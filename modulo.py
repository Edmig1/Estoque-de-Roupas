import customtkinter as tk

def criarjanela(Titulo,Tamanho,Tipo,Redimensionar=False):
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

def criar_label(local,texto,linha,coluna):
    label = tk.CTkLabel(local,text=texto)
    label.grid(row=linha, column=coluna)
    return label

def criar_input(local,placeholder,width,height,linha,coluna):
    input = tk.CTkEntry(local,placeholder_text=placeholder,width=width,height=height)
    input.grid(row=linha, column=coluna)
    return input

def criar_btn(local,texto,comando,width,height,linha,coluna,cor):
    btn = tk.CTkButton(local,text=texto,command=comando,width=width,height=height,fg_color=cor)
    btn.grid(row=linha, column=coluna)
    return btn
def criar_check(local,texto,linha,coluna):
    check = tk.CTkCheckBox(local,text=texto)
    check.grid(row=linha, column=coluna)
    return check

def criar_switch(local,texto,linha,coluna):
    switch = tk.CTkSwitch(local,text=texto)
    switch.grid(row=linha, column=coluna)
    return switch

def criar_combo(local,width,height,lista,linha,coluna):
    combo = tk.CTkComboBox(local,width=width,height=height,values=lista, state='readonly')
    combo.grid(row=linha, column=coluna)
    combo.set('Escolha a pessoa')
    return combo
def criar_barra(local,width,height,linha,coluna):
    barra = tk.CTkProgressBar(local,width=width,height=height)
    barra.grid(row=linha, column=coluna)
    return barra

def criar_slider(local,width,height,linha,coluna):
    slider = tk.CTkSlider(local,width=width,height=height)
    slider.grid(row=linha, column=coluna)
    return slider
