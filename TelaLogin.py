import time

import customtkinter as tk
from Modulos import *
from BDTemp import *

tk.set_appearance_mode("Light")
tk.set_default_color_theme("themes/violet.json")


def AlterarTema():
    if SwTemas.get()==1:
        tk.set_appearance_mode("dark")
        Titulo.configure(text_color="white")
        check.configure(text_color="white")
        imageFrame.configure(fg_color="#161515")
        contentFrame.configure(fg_color=janela.cget("bg"))

    else:
        tk.set_appearance_mode("light")
        Titulo.configure(text_color="black")
        check.configure(text_color="black")
        imageFrame.configure(fg_color="#F6F4F4")
        contentFrame.configure(fg_color=janela.cget("bg"))


def Clique():
    Login = Login_input.get()
    Senha = Senha_input.get()
    Resposta= AutenticarBD(Login,Senha)
    match Resposta:
        case "Certo":
            Titulo_Imagem = CriarLabel(janela, "Login feito com sucesso", 4, 0)
            Titulo_Imagem.grid(columnspan=12)
            Titulo_Imagem.configure(text_color="Green", font=("Arial", 16))
            from Tela2 import deiconify
            janela.withdraw()
            deiconify()
        case "Errado!":
            Titulo_Imagem = CriarLabel(janela, "Login / Senha incorretos", 4, 0)
            Titulo_Imagem.grid(columnspan=12)
            Titulo_Imagem.configure(text_color="Red", font=("Arial", 16))


def Cadastro():
    Abas_Login.set("Cadastro")



janela = CriarJanela("Janela", "800x350", 1)
imageFrame = CriarFrame(janela, 0, 0, 400, 350)
imageFrame.configure(fg_color="#F6F4F4")
imagem = CriarImagem(imageFrame, 300, 300, 2, 0, 'roupa.png')
imagem.grid(columnspan=13)
Titulo_Imagem = CriarLabel(imageFrame,"Entre com sua conta e gerencie o estoque", 0, 0)
Titulo_Imagem.configure(font=("Arial",18))
Titulo_Imagem.grid(columnspan=13)


contentFrame = CriarFrame(janela, 0, 1, 400, 350)
contentFrame.configure(fg_color=janela.cget("bg"))


Abas_Login = CriarAbas(contentFrame,1,1,300,300,"Login","Cadastro",)
Abas_Login.grid(columnspan=13)

Titulo = CriarLabel(Abas_Login.tab("Login"), "LOGIN", 2, 0)
Titulo.grid(columnspan=12)
Titulo.configure(text_color="Black", font=("Arial",30))
Login_input = CriarCaixaDeTexto(Abas_Login.tab("Login"),Largura=200, Altura=30, Linha=5, Coluna=6, Texto="Insira seu nome")
Senha_input = CriarCaixaDeTexto(Abas_Login.tab("Login"),Largura=200, Altura=30, Linha=6, Coluna=6, Texto="Insira sua senha",Modo="Senha")
check = CriarCheck(Abas_Login.tab("Login"),"Lembre de Mim", 7,6)
check.configure(text_color="Black", font=("Arial", 16))
check.get()
Btn_Logar = CriarBotao(Abas_Login.tab("Login"), Texto="LOGIN",Comando=Clique, Linha=8, Coluna=6, Largura=195, Altura=30)
SwTemas = CriarSwitch(contentFrame,"Alterar Tema  ",0,0,AlterarTema)
SwTemas.grid(columnspan=13, sticky = "E")


BtnCadastro= CriarBotao(Abas_Login.tab("Login"), "Cadastre-se", Cadastro, 30, 100, 10,6)


# ------------------------ Cadastro ---------------------------


def Voltar():
    Abas_Login.set("Login")




def LimparCax():
   Cx_Cad_ConfSenha.delete(0,"end")
   Cx_Cad_Senha.delete(0,"end")
   Cx_Cad_Login.delete(0,"end")
   Cx_Cad_Nome.delete(0,"end")
   Cx_Cad_CPF.delete(0,"end")
   Cx_Cad_DataNas.delete(0,"end")


   caixas_texto = [Cx_Cad_ConfSenha, Cx_Cad_Senha, Cx_Cad_Login, Cx_Cad_Nome, Cx_Cad_CPF, Cx_Cad_DataNas]
   for cx in caixas_texto:
       cx.delete(0, "end")


   Cb_Cad_Genero.set("Selecione")


def Cadastrar():
    Login = Cx_Cad_Login.get()
    Nome = Cx_Cad_Nome.get()
    CPF = Cx_Cad_CPF.get()
    Genero = Cb_Cad_Genero.get()
    Data = Cx_Cad_DataNas.get()
    Senha = Cx_Cad_Senha.get()
    if (Login and Nome and CPF and Genero != "Selecione" and Data and Senha):
        CadastrarBD(Login, Nome, CPF, Genero, Data, Senha)
        LimparCax()
        Lb_Cad_Erro.configure(text="Seu cadastro foi efetuado")
    else:
        Lb_Cad_Erro.configure(text="Confira os campos novamente")




###########   Tela de Cadastro   ###########
# Login
Lb_Cad_Login = CriarLabel(Abas_Login.tab("Cadastro"),"Login:",0,5)
Lb_Cad_Login.grid(sticky = "S")
Cx_Cad_Login = CriarCaixaDeTexto(Abas_Login.tab("Cadastro"),150,30,0,6,"Login")
Cx_Cad_Login.grid(sticky = "S")


# Nome
Lb_Cad_Nome = CriarLabel(Abas_Login.tab("Cadastro"), "Nome:", 1, 5)
Lb_Cad_Nome.grid(sticky="S")
Cx_Cad_Nome = CriarCaixaDeTexto(Abas_Login.tab("Cadastro"), 150, 30, 1, 6, "Nome")
Cx_Cad_Nome.grid(sticky="S")

# CPF
Lb_Cad_CPF = CriarLabel(Abas_Login.tab("Cadastro"), "CPF:", 2, 5)
Lb_Cad_CPF.grid(sticky="S")
Cx_Cad_CPF = CriarCaixaDeTexto(Abas_Login.tab("Cadastro"), 150, 30, 2, 6, "CPF", Modo="CPF")
Cx_Cad_CPF.grid(sticky="S")

# Gênero
Lb_Cad_Genero = CriarLabel(Abas_Login.tab("Cadastro"), "Gênero:", 3, 5)
Lb_Cad_Genero.grid(sticky="S")
Cb_Cad_Genero = CriarComboBox(Abas_Login.tab("Cadastro"), 150, 30, ["Masculino", "Feminino", "Outro"], 3, 6, )
Cb_Cad_Genero.grid(sticky="S")

# Data de Nascimento
Lb_Cad_DataNas = CriarLabel(Abas_Login.tab("Cadastro"), "Data de \nNascimento:", 4, 5)
Lb_Cad_DataNas.grid(sticky="S")
Cx_Cad_DataNas = CriarCaixaDeTexto(Abas_Login.tab("Cadastro"), 150, 30, 4, 6, "Data de nascimento", Modo="Data")
Cx_Cad_DataNas.grid(sticky="S")

# Senha
Lb_Cad_Senha = CriarLabel(Abas_Login.tab("Cadastro"), "Senha: ", 5, 5)
Lb_Cad_Senha.grid(sticky="S")
Cx_Cad_Senha = CriarCaixaDeTexto(Abas_Login.tab("Cadastro"), 150, 30, 5, 6, "Senha", Modo="Senha")
Cx_Cad_Senha.grid(sticky="S")

# Confirmar Senha
Lb_Cad_ConfSenha = CriarLabel(Abas_Login.tab("Cadastro"), "Confirme sua senha: ", 6, 5)
Lb_Cad_ConfSenha.grid(sticky="S")
Cx_Cad_ConfSenha = CriarCaixaDeTexto(Abas_Login.tab("Cadastro"), 150, 30, 6, 6, "Confirmação", Modo="Senha")
Cx_Cad_ConfSenha.grid(sticky="S")

# Mensagem de Erro
Lb_Cad_Erro = CriarLabel(Abas_Login.tab("Cadastro"), " ", 7, 0)
Lb_Cad_Erro.grid(columnspan=13)

# Botões
Btn_Cad_Cadastrar = CriarBotão(Abas_Login.tab("Cadastro"), "Cadastrar", Cadastrar, 8, 0, 100, 30)
Btn_Cad_Cadastrar.grid(columnspan=13)
Btn_Cad_Voltar = CriarBotão(Abas_Login.tab("Cadastro"), "Voltar", Voltar, 9, 0, 100, 30)
Btn_Cad_Voltar.grid(columnspan=13)



janela.mainloop()