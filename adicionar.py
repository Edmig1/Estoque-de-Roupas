from modulo import *
from ClasseProduto import *
qty = 0
total = 0
objeto = 0
preco = 0
name = ''

def abrirTela(nome):
    janelinha.deiconify()
    getTotal(nome)

def getTotal(nome):
    global total
    global objeto
    global name
    global preco
    for obj in ListaProdutos:
        if obj.nome == nome:
            name = obj.nome
            preco = obj.preco
            objeto = obj
            total = int(obj.estoque)
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
    qty += 1
    total += 1
    totalLabel.configure(text=f"Total: {total}")
    numero.configure(text=qty)

def confirma():
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

janelinha = CriarJanela("Adicionar estoque", "400x200", 2)
titulo1 = CriarLabel(janelinha, "Adicionar estoque",0,6)
titulo1.configure(font=("Arial",22))
numero = CriarLabel(janelinha, "0", 5, 6)
numero.configure(font=("Arial",42))
menos = CriarBotão(janelinha, "-", diminuir, 5, 5, 40,40)
menos.configure(font=("Arial",42))
mais = CriarBotão(janelinha, "+", aumentar, 5, 7, 40,40)
mais.configure(font=("Arial",42))
totalLabel = CriarLabel(janelinha,f"Total: {total}",12,6)
confirma = CriarBotão(janelinha, "Confirmar", confirma, 8,6,80,20)