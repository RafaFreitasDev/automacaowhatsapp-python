# Automação de encaminhamento de mensagens no whatsapp
# Usando a funcionalidade nativa do whatsapp de encaminhamento de mensagem
# Encaminhar de 5 em 5 mensagens

# libs - selenium pyperclip webdriver-manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.keys import Keys
import pyperclip
from selenium.webdriver.common.action_chains import ActionChains
import math

# instalação no manager-webdriver se necessário
service = Service(ChromeDriverManager().install())

# abrindo um navegador automatizado
nav = webdriver.Chrome(service=service)
nav.get('https://web.whatsapp.com')

sleep(20)


# Fechar o navegador
# nav.quit()

msn = '''
Mensagem teste!
Desconsire esta mensagem.
Isso está sendo mandado automaticamente.
'''

lista_contatos = ['Documento carro', 'Lembrete', 'Ligações indevidas', 'Plano de Recuperação', 'Animes', 'Rafinha', 'Henry']

# enviar msn para mim mesmo e depois encaminhar
# 1-clicar na lupa
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/button/div[2]/span').click()
# 2-pesquisar "eu mesmo"
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys('Eu mesmo')
# 3-dá um "enter"
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.ENTER)

sleep(2)

# 4(outra opção)-escrever msn para vc mesmo
# nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(msn)

# 4-copiar mensagem (evitar erro em caso de emoji)
pyperclip.copy(msn)
# 5-colar a mensagem na caixa de texto
nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.CONTROL + 'v')
# 6-enviar msn para vc mesmo
nav.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.ENTER)

sleep(2)

# como só pode encaminhar até 5 contatos, vamos contar quantas vezes precisaremos repetir 
qt_contatos = len(lista_contatos)
if qt_contatos % 5 == 0:
    qt_loops = qt_contatos / 5
else:
    qt_loops = math.floor(qt_contatos / 5) + 1

print(qt_loops)

# rodar o código de encaminhar
for i in range(qt_loops):
    i_inicial = i * 5 
    i_final = (i + 1) * 5
    lista_enviar = lista_contatos[i_inicial:i_final]

    # encaminhar a mensagem para a lista de contatos
    # clicar na setinha da mensagem (para encaminha)

    # 1-achar caixa de texto(elemento)
    lista_elementos = nav.find_elements('class name', 'UzMP7')
    for item in lista_elementos:
        msn = msn.replace('\n','')
        texto = item.text.replace('\n','')
        if msn in texto:
            elemento = item
            
    # 2-colocar o mouse em cima da mensagem
    ActionChains(nav).move_to_element(elemento).perform()
    # 3-clicar na setinha
    elemento.find_element('class name', '_3u9t-').click()
    sleep(0.5)
    # 4-clicar no nome encaminhar (na janelinha que abriu)
    nav.find_element('xpath', '//*[@id="app"]/div/span[4]/div/ul/div/li[4]/div').click()
    sleep(0.5)
    # 5-clicar botão (canto inf. esq.) de encaminhar
    nav.find_element('xpath', '//*[@id="main"]/span[2]/div/button[4]/span').click()
    sleep(1)

    # selecionar o 5 contatos para enviar
    for nome in lista_enviar:
        # escrevendo nome do contato
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(f'{nome}')
        sleep(0.7)
        # apertando enter
        nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
        sleep(0.7)
        
    sleep(2)
    nav.find_element('xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/span/div/div/div/span').click()
    sleep(3)






# Pausa a execução para permitir a inspeção manual
# input("Pressione Enter para fechar o navegador...")
