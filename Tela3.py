import customtkinter as tk
from modulo import *

class Produto:
    def __init__(self,nome,preco,qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = int(qtd)

camisa = Produto('camisa verde', 10.00, 10)
calca = Produto('calça azul', 10.00, 20)
jacket = Produto('jacket preto', 10.00, 30)

produtos = [camisa, calca, jacket]
verificacao = ['camisa verde', 'calça azul', 'jacket preto']
def comprar():
     for i in range(len(produtos)):
        if produtos[i].nome == combo1.get():
            if produtos[i].qtd >= int(input2.get()):
                produtos[i].qtd -= int(input2.get())
                sucesso = f'Suecesso! Unidades restantes:{produtos[i].qtd}'
                label2.configure(text=sucesso)
            else:
                label2.configure(text='Quantidade acima do limite aceitavel')

tk.set_appearance_mode("Light")
tk.set_default_color_theme('themes/violet.json')

janela = Criar_janela('Tela De Caixa','896x504',1)

label1 = Criar_label(janela,'Faça uma compra:',3,6)

combo1 = Criar_combo(janela, 200, 35, verificacao, 4,6)

input2 = Criar_input(janela,'Digite o Quantidade do Produto',200,35,5,6)
label2 = Criar_label(janela, '', 6,6)
label2.grid(sticky = "N")
btn = Criar_btn(janela,'Enviar',comprar,200,35,7,6,)




janela.mainloop()