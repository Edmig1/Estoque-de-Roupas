import customtkinter as tk
from modulo import *

tk.set_appearance_mode("Light")
tk.set_default_color_theme('themes/violet.json')

janela = Criar_janela('Tela De Caixa','896x504',2)

label1 = Criar_label(janela,'Faça uma compra:',3,6)

input1 = Criar_input(janela,'Digite o Nome do Produto',200,35,4,6)

input2 = Criar_input(janela,'Digite o Preço do Produto',200,35,5,6)

btn = Criar_btn(janela,'Enviar',comprar,200,35,7,6,)

input3 = Criar_input(janela,'Digite a quantidade do Produto',200,35,6,6)



janela.mainloop()