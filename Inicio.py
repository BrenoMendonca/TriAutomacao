#Importando a biblioteca
from PySimpleGUI import Button, Text, Window

window = Window(
    'Trantor',
    layout = [
        [Button('Teste')]          
              
              
              ]

)

window.read()


window.close()

def FazerLogin():
    try:

        login = input("Digite seu email Trilogo: ")
        senha = input("Digite sua senha: ")
        return login,senha
    except:
        print("Login ou senha inválidos, por favor digite novamente")  
FazerLogin()