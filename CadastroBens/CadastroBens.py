# Importando a biblioteca
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#Importando para leitura do Excel
import pandas as pd


#Criando a leitura de arquivo
Arquivo = 'Bens.xlsx'
#df = DataFrame
df = pd.read_excel(Arquivo)

# Atualizando o Chrome Driver Manager automaticamente
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Instalando o serviço do ChromeDriver usando o ChromeDriverManager
servico = Service(ChromeDriverManager().install())

# Inicializando o driver do Chrome com o serviço personalizado
navegador = webdriver.Chrome(service=servico)

#Acessando o dominio
navegador.get('https://comercial.trilogo.app')
time.sleep(2)

    #Solicitando os dados do usuario
#login = input("Digite seu email Trilogo: ")
#senha = input("Digite sua senha: ")
    

    #Inserindo dados de login
navegador.find_element('xpath','//*[@id="email"]').send_keys('breno.mendonca@trilogo.com.br')
navegador.find_element('xpath','//*[@id="password"]').send_keys('@Breno059')

navegador.find_element('xpath','//*[@id="submit"]').click()

time.sleep(3)  # Aguarda 03 segundos (pode ajustar esse valor)

Filiais_com_erro = [] #Criando o Array 
for index,row in df.iterrows():
        #pagina de cadastro
        navegador.get('https://comercial.trilogo.app/assets')
        time.sleep(2)
        #Novo bem
        navegador.find_element('xpath','//*[@id="root"]/div/div/div[2]/div[1]/div[2]/div/div/div[1]/button').click()
        time.sleep(2)
        navegador.find_element('xpath','//*[@id="patrimony"]').send_keys(row['Patrimonio'])
        navegador.find_element('xpath','//*[@id="description"]').send_keys(row['Descricao'])
        time.sleep(2)
        navegador.find_element('xpath','//*[@id="description"]').send_keys(Keys.ENTER)
        time.sleep(2)
        navegador.find_element('xpath','//*[@id="company"]').send_keys(row['Empresa'])
        time.sleep(2)
        navegador.find_element('xpath','//*[@id="company"]').send_keys(Keys.ENTER)
        time.sleep(2)
        navegador.find_element('xpath','//*[@id="type"]').send_keys(row['Tipo'])
        time.sleep(2)
        navegador.find_element('xpath','//*[@id="type"]').send_keys(Keys.ENTER)
        time.sleep(2)
        navegador.find_element('xpath','//*[@id="department"]').send_keys(row['Ambiente'])
        time.sleep(2)
        navegador.find_element('xpath','//*[@id="department"]').send_keys(Keys.ENTER)
        time.sleep(2)
        navegador.find_element('xpath','//*[@id="next"]').click()
        time.sleep(2)
        navegador.find_element('xpath','//*[@id="createAsset"]').click()
        time.sleep(2)


