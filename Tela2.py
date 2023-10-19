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
                print(produtos[i].nome)
                print(produtos[i].qtd)
                break
        produtos.pop()
        label1.configure(text='Produto Já Existente')
        label1.configure(text_color='#f0bc11')
    else:
        verificacao.append(input1.get())
        print(f'O número de itens cadastrados é: {len(produtos)}')
        label1.configure(text='Produto Adicionado Com Sucesso')
        label1.configure(text_color='lime')
janela = CriarJanela('Entrada de Produtos','1200x800','')
janela.iconbitmap('carreco.ico')


janela.mainloop()