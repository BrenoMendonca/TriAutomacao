#Importando a biblioteca
import customtkinter

#Iniciando a biblioteca
janela = customtkinter.CTk()
janela.geometry ("600x500")
janela.title("Trantor")

texto = customtkinter.CTkLabel(janela, text = "Bem Vindo!")
texto.pack(padx=30, pady = 30)

botao = customtkinter.CTkButton(janela, text= "Login")
botao.pack(padx = 10, pady = 10)

email  = customtkinter.CTkEntry(janela, placeholder_text = "Digite seu email")
email.pack(padx = 20, pady = 20)

senha  = customtkinter.CTkEntry(janela, placeholder_text = "Digite sua senha", show = "*")
senha.pack(padx = 20, pady = 20)

janela.mainloop()
