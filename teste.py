# Importando a biblioteca
import time
from selenium import webdriver

#Importando para leitura do Excel
import pandas as pd


#Criando a leitura de arquivo
Arquivo = 'Filiais.xlsx'

#df = DataFrame
df = pd.read_excel(Arquivo)

for index,row in df.iterrows():
    print(' Linha: ' + str(index) + "Nome da filial e  " + row["Nome da Filial"])



# Atualizando o Chrome Driver Manager automaticamente
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Instalando o serviço do ChromeDriver usando o ChromeDriverManager
servico = Service(ChromeDriverManager().install())

# Inicializando o driver do Chrome com o serviço personalizado
navegador = webdriver.Chrome(service=servico)


#Acessando o dominio
navegador.get('https://homologacao.trilogo.app/companies')

time.sleep(2)

#Solicitando os dados do usuario
login = input("Digite seu email Trilogo: ")
senha = input("Digite sua senha: ")
#Inserindo dados de login
navegador.find_element('xpath','//*[@id="email"]').send_keys(login)
navegador.find_element('xpath','//*[@id="password"]').send_keys(senha)
navegador.find_element('xpath','//*[@id="submit"]').click()

time.sleep(3)  # Aguarda 10 segundos (pode ajustar esse valor)

navegador.get('https://homologacao.trilogo.app/companies')

navegador.find_element('xpath','//*[@id="rc-tabs-0-panel-1"]/div/div/div/div[1]/div[1]/button').click()

#cadastrando o CNPJ da Unidade
navegador.find_element('xpath','//*[@id="cnpj"]').send_keys('42.054.740/0001-50')
navegador.find_element('xpath','/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
time.sleep(2)

#Modal de cadastro da Unidade
navegador.find_element('css selector', '#name').send_keys('13765-MULTIPLA-ER 24 DE OUTUBRO2')
navegador.find_element('xpath','//*[@id="account"]').send_keys('13765-MULTIPLA2')
time.sleep(2)
navegador.find_element('css selector', 'button[form="company-form"]').click()
time.sleep(5)


#ferramenta de estração de dados das páginas, p/ pegar os usuarios

