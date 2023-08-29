def CadastroCNPJ():
    # Importando a biblioteca
    import time
    from selenium import webdriver

    #Importando para leitura do Excel
    import pandas as pd


    #Criando a leitura de arquivo
    Arquivo = 'Filiais.xlsx'

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
    navegador.get('https://homologacao.trilogo.app')

    time.sleep(2)

    #Solicitando os dados do usuario
    login = input("Digite seu email Trilogo: ")
    senha = input("Digite sua senha: ")
    #Inserindo dados de login

    #TESTE
    navegador.find_element('xpath','//*[@id="email"]').send_keys(login)
    navegador.find_element('xpath','//*[@id="password"]').send_keys(senha)

    navegador.find_element('xpath','//*[@id="submit"]').click()

    time.sleep(3)  # Aguarda 03 segundos (pode ajustar esse valor)


    for index,row in df.iterrows():
        #pagina de cadastro
        navegador.get('https://homologacao.trilogo.app/companies')
        time.sleep(2)
        #Nova Unidade
        navegador.find_element('xpath','//*[@id="rc-tabs-0-panel-1"]/div/div/div/div[1]/div[1]/button').click()
        print(' \n Linha: ' + str(index) + " Nome da filial é  " + row["Nome da Filial"]+"\n")

        #cadastrando o CNPJ da Unidade
        
        navegador.find_element('xpath', '//*[@id="cnpj"]').send_keys(row['CNPJ'])
        time.sleep(2)
        
        navegador.find_element('xpath','/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]').click()
        time.sleep(2)
    
        try: 
            #Modal de cadastro da Unidade
            navegador.find_element('css selector', '#name').send_keys(row['Nome da Filial'])
            navegador.find_element('xpath','//*[@id="account"]').send_keys(row['Fantasia'])
            time.sleep(2)
            navegador.find_element('css selector', 'button[form="company-form"]').click()
            time.sleep(2)
            print('Próxima empresa 🤖')
        except:
            print("CNPJ INVALIDO ou já cadastrado " + row['CNPJ'])

            time.sleep(3)
            continue  

    print(" \n Fim do Programa! \n")


#ferramenta de estração de dados das páginas, p/ pegar os usuarios

