import customtkinter as tk
from modulo import *

tk.set_appearance_mode("Light")
tk.set_default_color_theme('themes/violet.json')

#----------------------------------------------------------------
produtos = []
verificacao = []

class Produto:
    def __init__(self,nome,preco,qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = int(qtd)

camisa = Produto('camisa verde', 10.00, 10)
calca = Produto('calça azul', 10.00, 10)
jacket = Produto('jacket preto', 10.00, 10)

produtos.append(camisa)
produtos.append(calca)
produtos.append(jacket)

verificacao = ['camisa verde', 'calça azul', 'jacket preto']

#-----------------------------------------------------------------
#functions

def gerarLista(objs, frame):
    for i in range(1, len(objs)):
        fr = CriarFrame(frame, i, 0, 750, 30)
        #fr.grid(sticky="N",rowspan=3)
        fr.configure(corner_radius=0)
        lt = Criar_label(fr, objs[i].nome, 6, 1)
        lt.grid(sticky="W")
        lp = Criar_label(fr, objs[i].preco, 6, 4)
        lp.grid(sticky="W")
        lq = Criar_label(fr, objs[i].qtd, 6, 6)
        lq.grid(sticky="W")



#janela
janela = Criar_janela('Tela De Caixa','896x504',2)
janela.iconbitmap('carreco.ico')

lista = CriarFrameScroll(janela, 5, 6, 730, 450)
hotBar = CriarFrame(janela, 4, 6, 750, 20)

#hotbar
pesquisa = Criar_input(hotBar, 'pesquise', 300, 20, 6, 0)
btnName = Criar_btn(hotBar, 'nome', 'orgname', 50, 20, 6, 10)
btnNum = Criar_btn(hotBar, 'nome', 'orgnum', 50, 20, 6, 11)

gerarLista(produtos, lista)
#grid config -------------------------
pesquisa.grid(sticky= 'W')

janela.mainloop()
