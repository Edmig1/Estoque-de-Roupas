class ClasseProduto():
    def __init__(self,nome,preco,desc,estoque,tipo):
        self.nome = nome
        self.preco = preco
        self.desc = desc
        self.estoque = estoque
        self.tipo = tipo

ListaProdutos = []
quantCompras = 0
quantVendas = 0
lucro = 0
maxEstoque = 300
percentEsto = 0

def addList (dado):
    ListaProdutos.append(dado)
    print(ListaProdutos)
def addComp (add):
    global quantCompras
    quantCompras += add

def comp ():
    global quantCompras
    return quantCompras

def addVend (add):
    global quantVendas
    quantVendas += add

def vendas ():
    global quantVendas
    return quantVendas

def atualizaLucro ():
    global quantCompras
    global quantVendas
    global lucro

    lucro = quantVendas - quantCompras
    return lucro

def calcSpace ():
    cont = 0
    for obj in ListaProdutos:
        cont += obj.estoque
    percent = cont / maxEstoque * 100
    return round(percent, 1)


camisa = ClasseProduto('camisa', 10, 'uma camisa', 15, 'Camiseta')
calca = ClasseProduto('calça', 10, 'uma calça', 12, 'Calças')
short = ClasseProduto('short preto', 10, 'um short', 11, 'Short')
vestido = ClasseProduto('vestido', 10, 'vestido', 10, 'Vestidos')
acessorio = ClasseProduto('relógio', 10, 'relogioeiro', 10, 'Acessórios')

addList(camisa)
addList(calca)
addList(short)
addList(vestido)
addList(acessorio)
