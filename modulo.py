import customtkinter as tk

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

def Criar_input(local,placeholder,width,height,linha,coluna):
    input = tk.CTkEntry(local,placeholder_text=placeholder,width=width,height=height)
    input.grid(row=linha, column=coluna)
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
    combo.set('Escolha a pessoa')
    return combo
def Criar_barra(local,width,height,linha,coluna):
    barra = tk.CTkProgressBar(local,width=width,height=height)
    barra.grid(row=linha, column=coluna)
    return barra

def Criar_slider(local,width,height,linha,coluna):
    slider = tk.CTkSlider(local,width=width,height=height)
    slider.grid(row=linha, column=coluna)
    return slider

#---------------Slider---------------
def CriarSlider(Local,Largura,Altura,Linha,Coluna):
    slider=Tk.CTkSlider(Local,width=Largura,height=Altura)
    slider.grid(row=Linha,column=Coluna)
    slider.set(0)
    return slider

#---------------Caixa de Texto (rolagem)---------------
def CriarTexto(Local,Linha,Coluna,Texto,Largura=0,Altura=0):
    caixatxt= tk.CTkTextbox(Local,wrap="word")
    caixatxt.grid(row=Linha,column=Coluna,sticky="nsew")
    caixatxt.insert("0.0",Texto,)
    if Largura!=0:
        caixatxt.configure(width=Largura)
    if Altura!=0:
        caixatxt.configure(height=Altura)

    return caixatxt



#---------------Imagem---------------
def CriarImagem(Local,Caminho,Linha, Coluna,Altura,Largura):
    imagem_pillow = Image.open(Caminho)
    imageTk = tk.CTkImage(imagem_pillow,size=[Largura,Altura])
    imagem = tk.CTkLabel(Local, image=imageTk, text= '')
    imagem.grid(row=Linha, column =Coluna)
    return imagem

def CriarData(Local,Linha,Coluna):
    pass

def CriarAbas(Local,Linha,Coluna,Largura,Altura,*Abas):
    aba = tk.CTkTabview(Local,width=Largura, height=Altura)
    for C in Abas:
        aba.add(C)
        Tamanho = list(range(13))
        aba.tab(C).grid_rowconfigure(Tamanho,weight=1)
        aba.tab(C).grid_columnconfigure(Tamanho, weight=1)
    aba.grid(row=Linha, column=Coluna)
    return aba

def CriarFrame(Local,Linha,Coluna,Largura,Altura):
    frame = tk.CTkFrame(Local,width=Largura,height=Altura)
    frame.grid(row=Linha, column=Coluna)
    Tamanho = list(range(13))
    frame.grid_propagate(False)
    frame.grid_rowconfigure(Tamanho, weight=1)
    frame.grid_columnconfigure(Tamanho, weight=1)
    return frame

def CriarFrameScroll(Local,Linha,Coluna,Largura,Altura):
    frame = tk.CTkScrollableFrame(Local,width=Largura,height=Altura)
    frame.grid(row=Linha, column=Coluna)
    Tamanho = list(range(13))
    frame.grid_rowconfigure(Tamanho, weight=1)
    frame.grid_columnconfigure(Tamanho, weight=1)
    return frame