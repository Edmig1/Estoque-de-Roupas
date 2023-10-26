from modulo import *
qty = 0
total = 34

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


janelasso = CriarJanela("Teste", "600x600", 1)
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
janelasso.mainloop()