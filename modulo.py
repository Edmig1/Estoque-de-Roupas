import customtkinter as tk
from PIL import Image

def Criar_janela(Titulo,Tamanho,Tipo,Redimensionar=False):
    if Tipo ==1:
        janela = tk.CTk()
    elif Tipo ==2:
        janela = tk.CTkToplevel()
    elif Tipo ==3:
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

def Criar_label(local,texto,linha,coluna):
    label = tk.CTkLabel(local,text=texto)
    label.grid(row=linha, column=coluna)
    return label

def Criar_input(local,placeholder,width,height,linha,coluna,modo ='padrao'):
    input = tk.CTkEntry(local,placeholder_text=placeholder,width=width,height=height)
    input.grid(row=linha, column=coluna)
    if modo == "senha":
        input.configure(show="*")
    elif modo == "moeda":
        def format_moeda(event=None):
            text = input.get().replace("R$", "")[:11]
            new_text = ""
            if event.keysym.lower() == "backspace": return
            for index in range(len(text)):
                if not text[index] in "0123456789": continue
                if index == 0:
                    new_text += "R$" + text[index]
                else:
                    new_text += text[index]
            input.delete(0, "end")
            input.insert(0, new_text)

        input.bind("<KeyRelease>", format_moeda)
    if modo == "CPF":
        def format_cpf(event=None):
            text = input.get().replace(".", "").replace("-", "")[:11]
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
            input.delete(0, "end")
            input.insert(0, new_text)

        input.bind("<KeyRelease>", format_cpf)
    elif modo == "CNPJ":
        def format_CNPJ(event=None):
            text = input.get().replace(".", "").replace("/", "").replace("-", "")[:14]
            new_text = ""
            if event.keysym.lower() == "backspace": return
            for index in range(len(text)):
                if not text[index] in "0123456789": continue
                if index == 0:
                    new_text += "(" + text[index]
                elif index == 7:
                    new_text += text[index] + "/"
                elif index == 11:
                    new_text += text[index] + "-"
                else:
                    new_text += text[index]
            input.delete(0, "end")
            input.insert(0, new_text)

        input.bind("<KeyRelease>", format_CNPJ)
    elif modo == "telefone":
        def format_tel(event=None):
            text = input.get().replace("(", "").replace(")", "").replace("-", "")[:11]
            new_text = ""
            if event.keysym.lower() == "backspace": return
            for index in range(len(text)):
                if not text[index] in "0123456789": continue
                if index == 0:
                    new_text += "(" + text[index]
                elif index == 1:
                    new_text += text[index] + ")"
                elif index == 5:
                    new_text += text[index] + "-"
                else:
                    new_text += text[index]
            input.delete(0, "end")
            input.insert(0, new_text)

        input.bind("<KeyRelease>", format_tel)
    elif modo == "data":
        def format_data(event=None):
            text = input.get().replace("/", "")[:8]
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
            input.delete(0, "end")
            input.insert(0, new_text)

        input.bind("<KeyRelease>", format_data)
    return input

def Criar_btn(local,texto,comando,width,height,linha,coluna):
    btn = tk.CTkButton(local,text=texto,command=comando,width=width,height=height,)
    btn.grid(row=linha, column=coluna)
    return btn
def Criar_check(local,texto,linha,coluna):
    check = tk.CTkCheckBox(local,text=texto)
    check.grid(row=linha, column=coluna)
    return check

def Criar_switch(local,texto,linha,coluna):
    switch = tk.CTkSwitch(local,text=texto)
    switch.grid(row=linha, column=coluna)
    return switch

def Criar_combo(local,width,height,lista,linha,coluna):
    combo = tk.CTkComboBox(local,width=width,height=height,values=lista, state='readonly')
    combo.grid(row=linha, column=coluna)
    combo.set('Selecione')
    return combo
def Criar_barra(local,width,height,linha,coluna):
    barra = tk.CTkProgressBar(local,width=width,height=height)
    barra.grid(row=linha, column=coluna)
    return barra

def Criar_slider(local,width,height,linha,coluna):
    slider = tk.CTkSlider(local,width=width,height=height)
    slider.grid(row=linha, column=coluna)
    return slider

def Criar_imagem(Local,Caminho,Linha, Coluna,Altura,Largura):
    imagem_pillow = Image.open(Caminho)
    imageTk = tk.CTkImage(imagem_pillow,size=[Largura,Altura])
    imagem = tk.CTkLabel(Local, image=imageTk, text= '')
    imagem.grid(row=Linha, column =Coluna)
    return imagem
