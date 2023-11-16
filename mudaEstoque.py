from modulo import *
from ClasseProduto import *
import customtkinter as tk

tk.set_appearance_mode(GetTema())
tk.set_default_color_theme('themes/violet.json')

quant = 0
reference = voltaTotalEsp()

def abrirTela():
    janelinha.deiconify()

def diminuir ():
    global quant
    global reference
    quant -= 1
    numero.configure(text=f'{reference + quant}')

def aumentar ():
    global reference
    global quant
    quant += 1
    numero.configure(text=f'{reference + quant}')

def confirmar ():
    global reference
    global quant
    alteraEs(reference + quant)

    from Tela4 import fecharAdd
    from Tela4 import atualizaTops
    atualizaTops()
    janelinha.withdraw()
    fecharAdd()


janelinha = CriarJanela("Adicionar estoque", "600x400", 2)
titulo1 = CriarLabel(janelinha, "Adicionar estoque",0,6)
titulo1.configure(font=("Arial",22))
numero = CriarLabel(janelinha, f'{reference}', 5, 6)
numero.configure(font=("Arial",42))
menos = CriarBotão(janelinha, "-", diminuir, 5, 5, 40,40)
menos.configure(font=("Arial",42))
mais = CriarBotão(janelinha, "+", aumentar, 5, 7, 40,40)
mais.configure(font=("Arial",42))
confirma = CriarBotão(janelinha, "Confirmar", confirmar, 8,6,80,20)
janelinha.mainloop()