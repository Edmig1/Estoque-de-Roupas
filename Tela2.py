import customtkinter as tk
from modulo import *
from ClasseProduto import *

ListaProdutos = []
verificacao = []

def enviar():
    inputs = [inputt2_1, inputt2_2, inputt2_3, inputt2_4]
    produto = ClasseProduto(inputt2_1.get(), inputt2_2.get(), inputt2_3.get(), inputt2_4.get(), inputt2_5.get())
    if inputt2_1.get() in verificacao:
        print(f'O produto {inputt2_1.get()} já está cadastrado')
        print(produto.nome)
    else:
        ListaProdutos.append(produto)
        verificacao.append(inputt2_1.get())
    for i in inputs:
        i.delete(0,'end')
    inputt2_5.set('Categoria')


tk.set_appearance_mode("Light")

tk.set_default_color_theme('themes/violet.json')

janela = CriarJanela('Entrada de Produtos','1920x1080',2)

framet2 = CriarFrame(janela,5,6,700,250)

framet2_2 = CriarFrame(janela,0,0,1920,80)

framet2_2.configure(fg_color='#EBEBEB')

imagem = CriarImagem(framet2_2,'BelleGlamour.png',6,0,100,400)

imagem2 = CriarImagem(framet2_2,'telefone.png',6,12,30,150)

framet2.configure(corner_radius=25)

framet2.configure(border_width=4,border_color='black')

labelt2 = CriarLabel(framet2,'Entrada de Produtos',1,1,'black')

labelt2.grid(columnspan=12)

framet2_2.grid(columnspan=13)

labelt2.configure(font=('Arial',27))

inputt2_1 = CriarCaixaDeTexto(framet2,200,40,4,6,'Nome:')

inputt2_2 = CriarCaixaDeTexto(framet2,200,40,5,6,'Preço:','Moeda')

inputt2_3 = CriarCaixaDeTexto(framet2,200,40,6,6,'Descrição:')

inputt2_4 = CriarCaixaDeTexto(framet2,200,40,4,7,'Estoque:')

inputt2_5 = CriarComboBox(framet2,200,40,['Camiseta','Short','Calças','Vestidos','Acessórios'],5,7)

btnt1_2 = CriarBotão(framet2,'ENVIAR',enviar,6,7,200,40)

btnt2_2 = CriarBotão(janela,'Controle De Estoque',enviar,9,6,200,40)

janela.mainloop()