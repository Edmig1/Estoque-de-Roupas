from modulo import *
from ClasseProduto import *
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
)

tk.set_appearance_mode(GetTema())
tk.set_default_color_theme('themes/violet.json')

def abrir4 ():
    janela4.deiconify()
    fresh(ListaProdutos)


def abrirAdd():
    from adicionar import abrirTela
    abrirTela()

def abrirRed():
    print()
    from reduzir import abrirTela
    abrirTela()

def fecharAdd():
    janela4.deiconify()
    fresh(ListaProdutos)

def open2():
    janela4.withdraw()
    from Tela2 import deiconify
    deiconify()

def mudaEstoque():
    from mudaEstoque import abrirTela
    janela4.withdraw()
    abrirTela()

#-----------------------------------------------------------------
#functions
def fresh (lista):
    cont = 0
    for obj in lista:
        card = CriarFrame(conteudo, cont, 0, larg - 60, 50)
        card.configure(fg_color=backColor)

        status = CriarFrame(card, 6, 0, 15, 15)
        status.configure(corner_radius=100)

        if float(obj.estoque) <= 0:
            status.configure(fg_color='red')
        else:
            status.configure(fg_color='green')

        match obj.tipo:
            case 'Camiseta':
                image = 'camisa.png'
            case 'Short':
                image = 'short.png'
            case 'Calças':
                image = 'calca.png'
            case 'Vestidos':
                image = 'vestido.png'
            case 'Acessórios':
                image = 'relogio.png'
            case _:
                image = 'camisa.png'


        im = CriarImagem(card, f'img/{image}',6, 1, 45, 45)
        im.grid(sticky='w')

        fTitle = CriarFrame(card, 6, 2, 100, 50)
        fTitle.configure(fg_color=backColor)
        fTitle.grid(sticky='w')
        title = CriarLabel(fTitle, obj.nome, 6, 2)
        title.configure(font=('inter', 18))
        title.grid(sticky='w')

        fcategoria = CriarFrame(card, 6, 4, 100, 40)
        fcategoria.configure(fg_color=backColor)
        categoria = CriarLabel(fcategoria, obj.tipo, 6, 4)
        categoria.configure(font=('inter', 18))
        fcategoria.grid(sticky='w')
        categoria.grid(sticky='w')

        desc = CriarLabel(card, obj.desc, 6, 6)
        desc.configure(font=('inter', 18))
        desc.grid(sticky='w')

        numtx = CriarLabel(card, obj.estoque, 6, 8)
        numtx.configure(font=('inter', 18))
        numtx.grid(sticky='w')

        preco = CriarLabel(card, obj.preco, 6, 10)
        preco.configure(font=('inter', 18))
        preco.grid(sticky='w')

        cont += 1

def atualizaTops ():
    # --
    itensEstoque = CriarFrame(infoCampo, 7, 0, largQuad, 115)
    itensEstoque.configure(fg_color=backColor)

    intesInfoE = CriarFrame(itensEstoque, 13, 0, largQuad, 85)
    intesInfoE.configure(fg_color=backColor, border_color=borderColor, border_width=2)

    estoInf = CriarBotão(intesInfoE, f'estoque em: {calcSpace()}%', mudaEstoque, 6, 2, largQuad - 20, 50)
    estoInf.configure(font=('inter', 20), fg_color=backColor)
    if GetTema() == 'light':
        estoInf.configure(text_color='black')

    itensImg = CriarFrame(itensEstoque, 5, 0, 108, 30)
    itensImg.configure(fg_color=principalColor)
    itensImg.grid(sticky='w')

    esto = CriarLabel(itensImg, 'estoque', 0, 6)
    esto.configure(text_color=backColor, font=('inter', 18))

    if calcSpace() >= 100:
        intesInfoE.configure(fg_color='#fcad03')

    # ------

    itensVendas = CriarFrame(infoCampo, 7, 4, largQuad, 115)
    itensVendas.configure(fg_color=backColor)

    intesInfoV = CriarFrame(itensVendas, 13, 0, largQuad, 85)
    intesInfoV.configure(fg_color=backColor, border_color=borderColor, border_width=2)

    vendInf = CriarLabel(intesInfoV, f'total de vendas: {vendas()}', 6, 2)
    vendInf.configure(font=('inter', 20))

    itensImgV = CriarFrame(itensVendas, 5, 0, 108, 30)
    itensImgV.configure(fg_color=principalColor)
    itensImgV.grid(sticky='w')

    vend = CriarLabel(itensImgV, 'vendas', 0, 6)
    vend.configure(text_color=backColor, font=('inter', 18))

    # ------

    itensEntrada = CriarFrame(infoCampo, 7, 8, largQuad, 115)
    itensEntrada.configure(fg_color=backColor)

    intesInfoEntra = CriarFrame(itensEntrada, 13, 0, largQuad, 85)
    intesInfoEntra.configure(fg_color=backColor, border_color=borderColor, border_width=2)

    entreInf = CriarLabel(intesInfoEntra, f'total de entrada: {comp()}', 6, 2)
    entreInf.configure(font=('inter', 20))

    itensImgE = CriarFrame(itensEntrada, 5, 0, 108, 30)
    itensImgE.configure(fg_color=principalColor)
    itensImgE.grid(sticky='w')

    entra = CriarLabel(itensImgE, 'entradas', 0, 6)
    entra.configure(text_color=backColor, font=('inter', 18))

    # --

    itensLucro = CriarFrame(infoCampo, 7, 12, largQuad, 115)
    itensLucro.configure(fg_color=backColor)

    intesInfoL = CriarFrame(itensLucro, 13, 0, largQuad, 85)
    intesInfoL.configure(fg_color=backColor, border_color=borderColor, border_width=2)

    lucInf = CriarLabel(intesInfoL, f'total de lucro: {atualizaLucro()}', 6, 2)
    lucInf.configure(font=('inter', 20))

    itensImgL = CriarFrame(itensLucro, 5, 0, 108, 30)
    itensImgL.configure(fg_color=principalColor)
    itensImgL.grid(sticky='w')

    luc = CriarLabel(itensImgL, 'Balanço', 0, 6)
    luc.configure(text_color=backColor, font=('inter', 18))
    luc.grid(sticky='w')

def nameOrg ():
    names = []
    secondL = []
    for i in ListaProdutos:
        names.append(i.nome)

    names.sort()
    for i in names:
        for j in ListaProdutos:
            if i == j.nome:
                secondL.append(j)

    fresh(secondL)

def numOrg():
    nuns = []
    secondL = []
    print(ListaProdutos)
    for i in ListaProdutos:
        nuns.append(i.estoque)
    print(nuns)
    nuns.sort(reverse=True)
    ll = []
    for i in ListaProdutos:
        ll.append(i)
    for i in nuns:
        for j in ll:
            if i == j.estoque:
                secondL.append(j)
                ll.remove(j)
    fresh(secondL)

def precoOrg ():
    nuns = []
    secondL = []
    for i in ListaProdutos:
        nuns.append(i.preco)
    nuns.sort(reverse=True)
    print(nuns)
    ll = []
    for i in ListaProdutos:
        ll.append(i)
    for i in nuns:
        for j in ll:
            if i == j.preco:
                secondL.append(j)
                ll.remove(j)
    fresh(secondL)

#add grafic
def atualizaGrafic ():
    figura = plt.Figure(figsize=(8,4), dpi=70)
    ax = figura.add_subplot(111)

    canva = FigureCanvasTkAgg(figura, graficos)
    canva.get_tk_widget().grid(row=6, column=0)

    data = {}
    dataComp = {}

    for i in ListaProdutos:
        data[i.nome] = i.vendas
        dataComp[i.nome] = i.compras

    product = data.keys()
    vend = data.values()

    ax.bar(product,vend)
    ax.set_title('vendas por produto')

    #-----other grafic---
    figura2 = plt.Figure(figsize=(8, 4), dpi=70)
    ax2 = figura2.add_subplot(111)

    canva2 = FigureCanvasTkAgg(figura2, graficos)
    canva2.get_tk_widget().grid(row=6, column=12)

    productComp = dataComp.keys()
    compr = dataComp.values()

    ax2.bar(productComp, compr)
    ax2.set_title('compras por produto')



#var -------------------------------------------------------------------------
larg = 1920
alt = 1080
backColor = GetCor()
borderColor = '#000000'
principalColor = '#7C63A6'

#header
altH = 80

#infos
largQuad = 200

#tabela
fontCol = 18

janela4 = CriarJanela('Dashboard', f'{larg}x{alt}', 2)
janela4.configure(fg_color=backColor)

#header
header = CriarFrame(janela4, 0, 0, larg, altH)
header.grid(sticky='n')
header.configure(fg_color=backColor)

logo = CriarImagem(header, 'img/logo.png', 7, 0, altH + 10,330)
logo.grid(sticky='w')

suporte = CriarImagem(header, 'img/suporte.png', 7, 12, altH - 20, 170)

#campos de informações
infoCampo = CriarFrame(janela4, 1, 0, larg, 115)
infoCampo.configure(fg_color=backColor)

atualizaTops()

#gráficos
graficos = CriarFrame(janela4, 2, 0, larg, 150)
graficos.configure(fg_color= GetCor())
atualizaGrafic()

#tabela
tabela = CriarFrame(janela4, 3, 0, larg - 680, 320)
tabela.configure(fg_color=backColor, border_color=principalColor, border_width=3)

colunas = CriarFrame(tabela, 0, 0, larg - 680, 50)
colunas.configure(fg_color=backColor, border_color=principalColor, border_width=3)
colunas.grid(sticky='n')

nome = CriarBotão(colunas, 'Nome', nameOrg, 7, 3, 50, 25, backColor, '#8259DC')
nome.configure(font=('inter', fontCol), text_color='black')

categoria = CriarLabel(colunas, '  Categoria', 7, 5)
categoria.configure(font=('inter', fontCol))
categoria.grid(stick='e')

desc = CriarLabel(colunas, '            Descrição', 7, 6)
desc.configure(font=('inter', fontCol))
desc.grid(stick='e')


num = CriarBotão(colunas, 'Número', numOrg, 7, 8, 50, 25, backColor, '#8259DC')
num.configure(font=('inter', fontCol), text_color='black')
num.grid(sticky='e')

preco = CriarBotão(colunas, 'Preço', precoOrg, 7, 9, 50, 25, backColor,'#8259DC' )
preco.configure(font=('inter', fontCol), text_color='black')
preco.grid(sticky='e')

#content table

conteudo = CriarFrameScroll(tabela, 1, 0, larg - 680, 270)
conteudo.configure(fg_color=janela4.cget('bg'), border_color=principalColor, border_width=3)

toHome = CriarFrame(janela4, 4, 0, larg, 50)
toHome.configure(fg_color=backColor)

addBtn = CriarBotão(toHome, 'Adicionar', abrirAdd, 6, 5, 100, 70, principalColor, '#6C5090')

lessBtn = CriarBotão(toHome, 'Reduzir', abrirRed, 6, 6, 100, 70, principalColor, '#6C5090')

voltarBtn = CriarBotão(toHome, 'retornar', open2, 6, 7, 100, 70, principalColor, '#6C5090')

fresh(ListaProdutos)


janela4.mainloop()