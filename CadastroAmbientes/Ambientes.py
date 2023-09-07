   # Importando a biblioteca
import time
from selenium import webdriver

    #Importando para leitura do Excel
import pandas as pd


    #Criando a leitura de arquivo
Arquivo = 'Meus Ambientes.xlsx'
df = pd.read_excel(Arquivo)

    # Atualizando o Chrome Driver Manager automaticamente
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

    # Instalando o serviço do ChromeDriver usando o ChromeDriverManager
servico = Service(ChromeDriverManager().install())

    # Inicializando o driver do Chrome com o serviço personalizado
navegador = webdriver.Chrome(service=servico)



    #Acessando o dominio
navegador.get('https://gruponatureza.trilogo.app')


time.sleep(2)

    #Solicitando os dados do usuario
login = input("Digite seu email Trilogo: ")
senha = input("Digite sua senha: ")
    

    #Inserindo dados de login
navegador.find_element('xpath','//*[@id="email"]').send_keys(login)
navegador.find_element('xpath','//*[@id="password"]').send_keys(senha)

navegador.find_element('xpath','//*[@id="submit"]').click()

time.sleep(3)  # Aguarda 03 segundos (pode ajustar esse valor)

navegador.get('https://gruponatureza.trilogo.app/departments')

time.sleep(2)
for index,row in df.iterrows():

        #Inserindo a Unidade e puxando a Unidade para o Loop
    navegador.find_element('css selector','div input[id=searchTerm]').send_keys(row['Unidades'])
    print(' \n Linha: ' + str(index) + " A filial que está sendo cadastrada é: " + row["Unidades"]+"\n")

    navegador.find_element('xpath','//*[@id="root"]/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div[1]/span/span/span/button').click()
    time.sleep(2)

    navegador.find_element('css selector','div button[class = addNewItem]').click()
    time.sleep(1)
        #Clicando no modal de cadastro de ambientes
    navegador.find_element('xpath','//*[@id="continueIncluding"]')
        #Preenchendo o modal
    #navegador.find_element('css selector', 'td input[id=name]').send_keys('Retaguarda')
    time.sleep(2)
    navegador.find_element('xpath', '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
    time.sleep(1)
    navegador.find_element('css selector', 'td input[id=name]').send_keys('Salão de Vendas')
    navegador.find_element('xpath', '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
    time.sleep(1)
    navegador.find_element('css selector', 'td input[id=name]').send_keys('Fachada')
    navegador.find_element('xpath', '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()




time.sleep(2)



