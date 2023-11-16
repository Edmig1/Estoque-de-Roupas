import subprocess
import time
import customtkinter as tk
from modulo import *
from ClasseProduto import *

def deiconify():
    janela2.deiconify()

def mudatexto():
    labelt2.configure(text='Entrada de Produtos')
    labelt2.configure(text_color='black')
verificacao = []
def enviar():
    inputs = [InputNome, InputPreco, InputDesc, InputEstoque]
    preco =InputPreco.get()
    preco = preco[2:len(preco)]
    preco = float(preco)
    print(preco)
    produto = ClasseProduto(InputNome.get(), preco, InputDesc.get(), InputEstoque.get(), ComboCat.get())
    if InputNome.get() in verificacao:
        labelt2.configure(text=f'Produto {InputNome.get()} já foi cadastrado')
        labelt2.configure(text_color='#fcad03')
        labelt2.after(3000,mudatexto)
    else:
        addList(produto)
        verificacao.append(InputNome.get())
        labelt2.configure(text=f'Produto {InputNome.get()} cadastrado com sucesso')
        labelt2.configure(text_color='#22b807')
        labelt2.after(3000,mudatexto)

    for i in inputs:
        i.delete(0,'end')
    ComboCat.set('Categoria')

def open4():
    from Tela4 import abrir4
    janela2.withdraw()
    abrir4()


tk.set_appearance_mode(GetTema())

tk.set_default_color_theme('themes/violet.json')

janela2 = CriarJanela('Entrada de Produtos','1920x1080',2)

framet2 = CriarFrame(janela2,5,6,700,250)

framet2_2 = CriarFrame(janela2,0,0,1920,80)

framet2_2.configure(fg_color= GetCor())

imagem = CriarImagem(framet2_2,'BelleGlamour.png',6,0,100,400)

imagem2 = CriarImagem(framet2_2,'telefone.png',6,12,30,150)

framet2.configure(corner_radius=25)

framet2.configure(border_width=4,border_color='black')

labelt2 = CriarLabel(framet2,'Entrada de Produtos',1,1,'black')

labelt2.grid(columnspan=12)

framet2_2.grid(columnspan=13)

labelt2.configure(font=('Arial',27))

InputNome = CriarCaixaDeTexto(framet2,200,40,4,6,'Nome:')

InputPreco = CriarCaixaDeTexto(framet2,200,40,5,6,'Preço:','Moeda')

InputDesc = CriarCaixaDeTexto(framet2,200,40,6,6,'Descrição:')

InputEstoque = CriarCaixaDeTexto(framet2,200,40,4,7,'Estoque:')

ComboCat = CriarComboBox(framet2,200,40,['Camiseta','Short','Calças','Vestidos','Acessórios'],5,7)

btnt1_2 = CriarBotão(framet2,'ENVIAR',enviar,6,7,200,40)

btnt2_2 = CriarBotão(janela2,'Controle De Estoque',open4,9,6,200,40)

janela2.mainloop()