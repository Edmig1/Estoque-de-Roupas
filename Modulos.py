import customtkinter as tk
from PIL import Image
primeiro = True

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
    Caixa = tk.CTkEntry(Local,width=Largura,height=Altura)
    Caixa.grid(row=Linha, column=Coluna)
    if Texto != "":
        Caixa.configure(placeholder_text=Texto)
    if Modo == "Senha":
        Caixa.configure(show="*")


def CriarBotao(Local,Texto,Comando,Altura,Largura,Linha,Coluna,Imagem="Nada"):
    if Imagem!="Nada":
        imagem_pillow = Image.open(Imagem)
        imageTk = tk.CTkImage(imagem_pillow, size=[15, 15])
        botao = tk.CTkButton(Local, text=Texto, command=Comando,
                             width=Largura, height=Altura, image=imageTk)
        botao.grid(row=Linha, column=Coluna)
    else:
        botao = tk.CTkButton(Local, text=Texto, command=Comando,
                             width=Largura, height=Altura)
        botao.grid(row=Linha, column=Coluna)

    return botao

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
    return slider


def CriarImagem(Local,Largura,Altura,Linha,Coluna,Caminho):
    image = Image.open(Caminho)
    imagetk = tk.CTkImage(image,size=[Largura,Altura])
    labelImage = tk.CTkLabel(Local,text=" ",image=imagetk)
    labelImage.grid(row=Linha,column=Coluna)
    return labelImage


def CriarFrame(Local,Linha,Coluna,Largura,Altura):
    frame = tk.CTkFrame(Local,width=Largura,height=Altura)
    frame.grid(row=Linha, column=Coluna)
    Tamanho = list(range(13))
    frame.grid_propagate(False)
    frame.grid_rowconfigure(Tamanho, weight=1)
    frame.grid_columnconfigure(Tamanho, weight=1)
    return frame

def CriarCaixaDeTexto(Local,Largura,Altura,Linha,Coluna,Texto=0,Modo="Padrão"):
    Caixa = tk.CTkEntry(Local,width=Largura,height=Altura)
    Caixa.grid(row=Linha,column=Coluna)
    if Texto!=0:
     Caixa.configure(placeholder_text=Texto)
    if Modo == "Senha":
        Caixa.configure(show="*")
        def SenhaMostra():
            global primeiro
            if primeiro:
                imagem_pillow = Image.open("eye.ico")
                imagetk = tk.CTkImage(imagem_pillow, size=[15, 15])
                MostraSenha.configure(image=imagetk)
                Caixa.configure(show="")
                primeiro = False
            else:
                imagem_pillow = Image.open("eye2.ico")
                imagetk = tk.CTkImage(imagem_pillow, size=[15, 15])
                MostraSenha.configure(image=imagetk)
                Caixa.configure(show="*")
                primeiro = True
        MostraSenha = CriarBotao(Caixa, "", SenhaMostra, 10, 10, 0, 0, Imagem="eye2.ico")
        MostraSenha.grid(sticky="e", padx=2)
        MostraSenha.configure(fg_color=Caixa.cget("fg_color"), hover_color=Caixa.cget("fg_color"), corner_radius=0)

        return Caixa

def CriarAbas(Local, Linha, Coluna, Largura, Altura, *Abas):
       aba = tk.CTkTabview(Local, width=Largura, height=Altura)
       for C in Abas:
           aba.add(C)
           Tamanho = list(range(13))
           aba.tab(C).grid_rowconfigure(Tamanho, weight=1)
           aba.tab(C).grid_columnconfigure(Tamanho, weight=1)
       aba.grid(row=Linha, column=Coluna)
       return aba



# ------------- Cadastro ----------------



def CriarLabel(Local,Texto,Linha,Coluna,Cor="black"):
   Label = tk.CTkLabel(Local,text=Texto)
   Label.grid(row=Linha,column=Coluna)
   if Cor!="black":
       Label.configure(text_color=Cor)
   return Label


def CriarComboBox(Local,Largura,Altura,Valores,Linha,Coluna,Comando=0):
   combo= tk.CTkComboBox(Local, width=Largura, height=Altura,
                         values=Valores, state="readonly")
   combo.grid(row=Linha, column=Coluna)
   combo.set("Selecione")
   if Comando!=0:
       combo.configure(command=Comando)
   return combo



def CriarTexto(Local,Linha,Coluna,Texto,Largura=0,Altura=0):
   caixatxt= tk.CTkTextbox(Local,wrap="word")
   caixatxt.grid(row=Linha,column=Coluna,sticky="nsew")
   caixatxt.insert("0.0",Texto,)
   if Largura!=0:
       caixatxt.configure(width=Largura)
   if Altura!=0:
       caixatxt.configure(height=Altura)


   return caixatxt



def CriarBotão(Local,Texto,Comando,Linha,Coluna,Largura,Altura,Cor=0,CorHover=0,Imagem="Nada"):
   if Imagem!="Nada":
       imagem_pillow = Image.open(Imagem)
       imageTk = tk.CTkImage(imagem_pillow, size=[15, 15])
       botao = tk.CTkButton(Local, text=Texto, command=Comando,
                            width=Largura, height=Altura, image=imageTk)
       botao.grid(row=Linha, column=Coluna)
   else:
       botao = tk.CTkButton(Local, text=Texto, command=Comando,
                            width=Largura, height=Altura)
       botao.grid(row=Linha, column=Coluna)
   if Cor != 0:
           botao.configure(fg_color=Cor)
   if CorHover != 0:
           botao.configure(hover_color=CorHover)


   return botao





def CriarCaixaDeTexto(Local,Largura,Altura,Linha,Coluna,Texto=0,Modo="Padrão"):
   Caixa = tk.CTkEntry(Local,width=Largura,height=Altura)
   Caixa.grid(row=Linha,column=Coluna)
   if Texto!=0:
    Caixa.configure(placeholder_text=Texto)
   if Modo == "Senha":
       Caixa.configure(show="*")
       def SenhaMostra():
           global primeiro
           if primeiro:
               imagem_pillow = Image.open("Imagens/eye.ico")
               imageTk = tk.CTkImage(imagem_pillow, size=[15, 15])
               MostraSenha.configure(image=imageTk)
               Caixa.configure(show="")
               primeiro = False
           else:
               imagem_pillow = Image.open("Imagens/eye2.ico")
               imageTk = tk.CTkImage(imagem_pillow, size=[15, 15])
               MostraSenha.configure(image=imageTk)
               Caixa.configure(show="*")
               primeiro = True
       MostraSenha = CriarBotão(Caixa, "", SenhaMostra, 0, 0, 10, 10, Imagem="eye2.ico")
       MostraSenha.grid(sticky="e", padx=2)
       MostraSenha.configure(fg_color=Caixa.cget("fg_color"), hover_color=Caixa.cget("fg_color"), corner_radius=0)


   elif Modo == "CPF":
       def format_cpf(event=None):
           text = Caixa.get().replace(".", "").replace("-", "")[:11]
           new_text = ""
           if event.keysym.lower() == "backspace": return
           for index in range(len(text)):


               if not text[index] in "0123456789": continue
               if index in [2, 5]:
                   new_text += text[index] + "."
               elif index == 8:
                   new_text += text[index] + "-"
               else:
                   new_text += text[index]
           Caixa.delete(0, "end")
           Caixa.insert(0, new_text)


       Caixa.bind("<KeyRelease>", format_cpf)


   elif Modo == "Data":
       def format_data(event=None):
           text = Caixa.get().replace("/", "")[:8]
           new_text = ""
           if event.keysym.lower() == "backspace":
               return
           for index in range(len(text)):
               if not text[index] in "0123456789":
                   continue
               if index in [1, 3]:
                   new_text += text[index] + "/"
               elif index == 9:
                   new_text += text[index]
               else:
                   new_text += text[index]
           Caixa.delete(0, "end")
           Caixa.insert(0, new_text)
       Caixa.bind("<KeyRelease>", format_data)

   return Caixa


