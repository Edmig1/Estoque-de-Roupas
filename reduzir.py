from modulo import *
from ClasseProduto import *

qty = 0
total = 0
objeto = 0
totalReal = 0
preco = 0
name = ''

def abrirTela(nome):
    jc.deiconify()
    getTotal(nome)

def getTotal(nome):
    global total
    global totalReal
    global objeto
    global preco
    global name
    for obj in ListaProdutos:
        if obj.nome == nome:
            name = obj.nome
            objeto = obj
            total = int(obj.estoque)
            totalReal = int(obj.estoque)
            preco = float(obj.preco)
            totalLabel.configure(text=f"Total: {total}")

def regra(total, parcial):
    porcento = parcial/total
    return porcento

def diminuir():
    global qty
    global total
    if qty != 0:
        qty -= 1
        total += 1
        totalLabel.configure(text=f"Total: {total}")
        numero.configure(text=qty)
        pb.set(value=regra(totalReal, total))

def aumentar():
    global qty
    global total
    if qty < 34:
        qty += 1
        total -= 1
        totalLabel.configure(text=f"Total: {total}")
        numero.configure(text=qty)
        pb.set(value=regra(totalReal, total))

def confirma():
    from Tela4 import fecharAdd
    from Tela4 import atualizaTops
    from Tela4 import fresh
    global objeto
    global total
    global preco
    global totalReal
    diferenca = totalReal - total
    addVend(diferenca * preco)
    for i in ListaProdutos:
        if i.nome == name:
            i.estoque = total
            break
    atualizaTops()
    fresh(ListaProdutos)
    jc.withdraw()
    fecharAdd()

jc = CriarJanela("Retirar estoque", "400x200", 2)
titulo1 = CriarLabel(jc, "Retirar estoque",0,6)
titulo1.configure(font=("Arial",22))
numero = CriarLabel(jc, "0", 5, 6)
numero.configure(font=("Arial",42))
menos = CriarBotão(jc, "-", diminuir, 5, 5, 40,40)
menos.configure(font=("Arial",42))
mais = CriarBotão(jc, "+", aumentar, 5, 7, 40,40)
mais.configure(font=("Arial",42))
pb = CriarProgressBar(jc,150,15,12, 6)
pb.grid(sticky="W")
pb.set(value=1)
totalLabel = CriarLabel(jc,f"Total: {total}",12,7)
confirma = CriarBotão(jc, "Confirmar", confirma, 8,6,80,20)