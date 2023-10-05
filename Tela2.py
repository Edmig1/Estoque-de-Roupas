import customtkinter as tk
from modulo import *
tk.set_appearance_mode("Light")
tk.set_default_color_theme('themes/violet.json')
class Produto:
    def __init__(self,nome,preco,qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = int(qtd)

produtos = []
verificacao = []

def enviar():
    produto = Produto(input1.get(), input2.get(), input3.get())
    produtos.append(produto)
    if input1.get() in verificacao:
        for i in range(len(produtos)):
            if produtos[i].nome == input1.get():
                produtos[i].qtd += int(input3.get())
                print(produtos[i].nome)
                print(produtos[i].qtd)
                break
        produtos.pop()
        label1.configure(text='Quantidade adicionada ao estoque')
        label1.configure(text_color='#f0bc11')
    else:
        verificacao.append(input1.get())
        print(f'O número de itens cadastrados é: {len(produtos)}')
        label1.configure(text='Produto Adicionado Com Sucesso')
        label1.configure(text_color='lime')

janela = Criar_janela('Tela De Caixa','896x504',2)
janela.iconbitmap('carreco.ico')


label1 = Criar_label(janela,'Adicione um Produto:',3,6)

input1 = Criar_input(janela,'Digite o Nome do Produto',200,35,4,6)

input2 = Criar_input(janela,'Digite o Preço do Produto',200,35,5,6)

btn = Criar_btn(janela,'Enviar',enviar,200,35,7,6,)

input3 = Criar_input(janela,'Digite a quantidade do Produto',200,35,6,6)

btn2 = Criar_btn(janela,'Saída de Produtos',enviar,200,35,12,3,)

btn3 = Criar_btn(janela,'Gerenciamento de Estoque',enviar,200,35,12,9,)

label1.configure(font=('Quicksand',24))
input1.configure(font=('Quicksand',12))
input2.configure(font=('Quicksand',12))
btn.configure(font=('Quicksand',12))
input3.configure(font=('Quicksand',12))

janela.mainloop()