from modulo import *
from ClasseProduto import *
import customtkinter as tk

tk.set_appearance_mode("Light")
tk.set_default_color_theme('themes/violet.json')

qty = 0
total = 0
objeto = 0
preco = 0
name = ''

def abrirTela():
    janelinha.deiconify()

def listar():
    tudo = []
    for i in ListaProdutos:
        tudo.append(i.nome)
    return tudo

def getTotal(nome):
    global total
    global objeto
    global name
    global preco
    global qty
    for obj in ListaProdutos:
        if obj.nome == nome:
            qty = 0
            name = obj.nome
            preco = obj.preco
            objeto = obj
            total = int(obj.estoque)
            numero.configure(text=qty)
            totalLabel.configure(text=f"Total: {total}")


def diminuir():
    global qty
    global total
    if qty != 0:
        qty -= 1
        total -= 1
        totalLabel.configure(text=f"Total: {total}")
        numero.configure(text=qty)
def aumentar():
    global qty
    global total
    if total != 0:
        qty += 1
        total += 1
        totalLabel.configure(text=f"Total: {total}")
        numero.configure(text=qty)

def confirmar():
    from Tela4 import fecharAdd
    from Tela4 import atualizaTops
    from Tela4 import fresh
    global objeto
    global total
    global name
    global preco
    addComp(preco * total)

    for i in ListaProdutos:
        if i.nome == name:
            i.estoque = total
            break

    atualizaTops()
    fresh(ListaProdutos)
    janelinha.withdraw()
    fecharAdd()

janelinha = CriarJanela("Adicionar estoque", "600x400", 2)
titulo1 = CriarLabel(janelinha, "Adicionar estoque",0,6)
titulo1.configure(font=("Arial",22))
opcoes = CriarComboBox(janelinha, 100,15, listar(), 2, 6)
opcoes.configure(command=getTotal)
numero = CriarLabel(janelinha, "0", 5, 6)
numero.configure(font=("Arial",42))
menos = CriarBotão(janelinha, "-", diminuir, 5, 5, 40,40)
menos.configure(font=("Arial",42))
mais = CriarBotão(janelinha, "+", aumentar, 5, 7, 40,40)
mais.configure(font=("Arial",42))
totalLabel = CriarLabel(janelinha,f"Total: {total}",12,6)
confirma = CriarBotão(janelinha, "Confirmar", confirmar, 8,6,80,20)
janelinha.mainloop()