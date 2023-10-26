import customtkinter as tk
from modulo import *

tk.set_appearance_mode("Light")
#tk.set_default_color_theme('themes/violet.json')

#----------------------------------------------------------------
produtos = []
verificacao = []

class Produto:
    def __init__(self,nome, categoria, descricao,preco,qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = int(qtd)
        self.descricao = descricao
        self.categoria = categoria

camisa = Produto('camisa verde', 'camisa', 'camisa verde', 10.00, 10)

produtos.append(camisa)

verificacao = ['camisa verde']

#-----------------------------------------------------------------
#functions
def fresh (lista):
    for obj in produtos:
        card = CriarFrame(conteudo, 0, 0, larg - 60, 50)
        card.configure(fg_color=backColor)

        status = CriarFrame(card, 6, 0, 15, 15)
        status.configure(corner_radius=100)

        if obj.qtd <= 0:
            status.configure(fg_color='red')
        else:
            status.configure(fg_color='green')

        match obj.categoria:
            case 'camisa':
                image = 'camisa.png'

        im = CriarImagem(card, f'img/{image}',6, 1, 45, 45)
        im.grid(sticky='w')

        title = CriarLabel(card, obj.nome, 6, 2)
        title.configure(font=('inter', 18))
        title.grid(sticky='w')

        division = CriarFrame(card, 6, 3, 3, 35)
        division.configure(fg_color='#8259DC')
        division.grid(sticky='w')

        categoria = CriarLabel(card, obj.categoria, 6, 4)
        categoria.configure(font=('inter', 18))
        categoria.grid(sticky='w')

        division = CriarFrame(card, 6, 5, 3, 35)
        division.configure(fg_color='#8259DC')
        division.grid(sticky='w')

        desc = CriarLabel(card, obj.descricao, 6, 6)
        desc.configure(font=('inter', 18))
        desc.grid(sticky='w')

        division = CriarFrame(card, 6, 7, 3, 35)
        division.configure(fg_color='#8259DC')
        division.grid(sticky='w')


        numtx = CriarLabel(card, obj.qtd, 6, 8)
        numtx.configure(font=('inter', 18))
        numtx.grid(sticky='w')

        division = CriarFrame(card, 6, 9, 3, 35)
        division.configure(fg_color='#8259DC')
        division.grid(sticky='w')

        preco = CriarLabel(card, obj.preco, 6, 10)
        preco.configure(font=('inter', 18))
        preco.grid(sticky='w')

        division = CriarFrame(card, 6, 11, 3, 35)
        division.configure(fg_color='#8259DC')
        division.grid(sticky='w')

        edit = CriarBotão(card, '', 'edit', 6, 12, 40, 25, '#8259DC', '#6A34E1', 'img/lapis.png')
        #edit.configure(fg_color='#8259DC')
        edit.grid(sticky='w')




#var -------------------------------------------------------------------------
larg = 1920
alt = 1080
backColor = '#ffffff'
borderColor = '#000000'
principalColor = '#8259dc'

#header
altH = 80

#infos
largQuad = 200

#tabela
fontCol = 18

janela4 = CriarJanela('Dashboard', f'{larg}x{alt}', 1)
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

#--
itensEstoque = CriarFrame(infoCampo, 7, 0, largQuad, 115)
itensEstoque.configure(fg_color=backColor)

intesInfoE = CriarFrame(itensEstoque, 13, 0, largQuad, 85)
intesInfoE.configure(fg_color=backColor, border_color=borderColor, border_width=2)

itensImg = CriarFrame(itensEstoque, 5, 0, 108, 30)
itensImg.configure(fg_color=principalColor)
itensImg.grid(sticky='w')

esto = CriarLabel(itensImg, 'estoque', 0, 6)
esto.configure(text_color=backColor, font=('inter', 18))

#------

itensVendas = CriarFrame(infoCampo, 7, 6, largQuad, 115)
itensVendas.configure(fg_color=backColor)

intesInfoV = CriarFrame(itensVendas, 13, 0, largQuad, 85)
intesInfoV.configure(fg_color=backColor, border_color=borderColor, border_width=2)

itensImgV = CriarFrame(itensVendas, 5, 0, 108, 30)
itensImgV.configure(fg_color=principalColor)
itensImgV.grid(sticky='w')

vend = CriarLabel(itensImgV, 'vendas', 0, 6)
vend.configure(text_color=backColor, font=('inter', 18))

#------

itensEntrada = CriarFrame(infoCampo, 7, 12, largQuad, 115)
itensEntrada.configure(fg_color=backColor)

intesInfoEntra = CriarFrame(itensEntrada, 13, 0, largQuad, 85)
intesInfoEntra.configure(fg_color=backColor, border_color=borderColor, border_width=2)

itensImgE = CriarFrame(itensEntrada, 5, 0, 108, 30)
itensImgE.configure(fg_color=principalColor)
itensImgE.grid(sticky='w')

entra = CriarLabel(itensImgE, 'entradas', 0, 6)
entra.configure(text_color=backColor, font=('inter', 18))

#gráficos
#graficos = CriarFrame(janela4, 2, 0, larg, 300)

#tabela
tabela = CriarFrame(janela4, 3, 0, larg - 680, 320)
tabela.configure(fg_color=backColor, border_color=principalColor, border_width=3)

colunas = CriarFrame(tabela, 0, 0, larg - 680, 50)
colunas.configure(fg_color=backColor, border_color=principalColor, border_width=3)
colunas.grid(sticky='n')

nome = CriarLabel(colunas, 'Nome', 7, 3)
nome.configure(font=('inter', fontCol))

categoria = CriarLabel(colunas, '  Categoria', 7, 5)
categoria.configure(font=('inter', fontCol))
categoria.grid(stick='e')

desc = CriarLabel(colunas, '            Descrição', 7, 6)
desc.configure(font=('inter', fontCol))
desc.grid(stick='e')


num = CriarLabel(colunas, '     Número', 7, 8)
num.configure(font=('inter', fontCol))
num.grid(sticky='e')

preco = CriarLabel(colunas, '                Preço', 7, 9)
preco.configure(font=('inter', fontCol))
preco.grid(sticky='w')

#content table

conteudo = CriarFrameScroll(tabela, 1, 0, larg - 680, 270)
conteudo.configure(fg_color=janela4.cget('bg'), border_color=principalColor, border_width=3)

fresh(produtos)


janela4.mainloop()
