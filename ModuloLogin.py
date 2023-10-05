import customtkinter as tk


def CriarJanela(Titulo,Tamanho,Tipo,Redimensionar=False):
    if Tipo == 1:
        janela = tk.CTk()
    elif Tipo == 2:
        janela = tk.CTkToplevel()
    elif Tipo == 3:
        janela = tk.CTkInputDialog()
    janela.title(Titulo)
    janela.geometry(Tamanho)
    if Redimensionar !=False:
        janela.resizable(width=True, height=True)
    else:
        janela.resizable(width=False, height=False)
    colunas = list(range(13))
    linhas = list(range(13))
    janela.grid_columnconfigure(colunas, weight=1)
    janela.grid_rowconfigure(linhas, weight=1)
    return janela


def CriarLabel(Local,Texto,Linha,Coluna):
    label = tk.CTkLabel(Local,text=Texto)
    label.grid(row=Linha, column=Coluna)
    return label


def CriarInput(Local,Largura, Altura,Linha,Coluna,Texto="", Modo="Padrão"):
    caixa = tk.CTkEntry(Local,width=Largura,height=Altura)
    caixa.grid(row=Linha, column=Coluna)
    if Texto != "":
        caixa.configure(placeholder_text=Texto)
    if Modo == "Senha":
        caixa.configure(show="*")
        def SenhaMostra():
            global primeiro
            if primeiro:
                imagem_pillow = Image.open("eye.ico")
                imageTk = Tk.CTkImage(imagem_pillow, size=[15, 15])
                MostraSenha.configure(image=imageTk)
                caixa.configure(show="")
                primeiro = False
    return caixa


def CriarBotao(Local,Texto,Comando,Altura,Largura,Linha,Coluna):
    btn = tk.CTkButton(Local,text=Texto, command=Comando, width=Largura, height=Altura)
    btn.grid(row=Linha, column=Coluna)
    return btn


def CriarCheck(Local,Texto, Linha, Coluna, Comando=False):
    check = tk.CTkCheckBox(Local,text=Texto)
    if Comando != False:
        check.configure(command=Comando)
    check.grid(row=Linha, column=Coluna)
    return check


def CriarSwitch(Local,Texto, Linha, Coluna, Comando=False):
    switch = tk.CTkSwitch(Local,text=Texto)
    if Comando != False:
        switch.configure(command=Comando)
    switch.grid(row=Linha, column=Coluna)
    return switch


def CriarComboBox(Local,Valor, Largura,Altura, Linha,Coluna, Comando=False):
    box = tk.CTkComboBox(Local,values=Valor,width=Largura,height=Altura, state="readonly")
    if Comando != False:
        box.configure(command=Comando)
    box.grid(row=Linha, column=Coluna)
    box.set("Selecione")
    return box


def CriarBar(Local,Largura,Altura,Linha,Coluna):
    bar = tk.CTkProgressBar(Local,width=Largura,height=Altura)
    bar.grid(row=Linha, column=Coluna)


def CriarSlider(Local,Largura,Altura,Linha,Coluna):
    slider = tk.CTkSlider(Local,width=Largura,height=Altura)
    slider.grid(row=Linha, column=Coluna)

def CriarImagem(Local,Largura,Altura,Linha,Coluna,Caminho):
    image = Image.open(Caminho)
    imagetk = tk.CTkImage(image,size=[Largura,Altura])
    labelImage = tk.CTkLabel(Local,text=" ",image=imagetk)
    labelImage.grid(row=Linha,column=Coluna)
    return labelImage