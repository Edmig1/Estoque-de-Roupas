import customtkinter as tk
from modulo import *
def enviar():
    pass
tk.set_appearance_mode("Light")
tk.set_default_color_theme('themes/violet.json')
janela = CriarJanela('Entrada de Produtos','854x480',2)
framet2 = CriarFrame(janela,7,6,700,250)
framet2.configure(corner_radius=25)
framet2.configure(border_width=4,border_color='black')
labelt2 = CriarLabel(framet2,'Entrada de Produtos',1,1,'black')
labelt2.grid(columnspan=12)
labelt2.configure(font=('Arial',27))
inputt2_1 = CriarCaixaDeTexto(framet2,200,40,4,6,'Nome:')
inputt2_1 = CriarCaixaDeTexto(framet2,200,40,5,6,'Preço:')
inputt2_1 = CriarCaixaDeTexto(framet2,200,40,6,6,'Descrição:')
inputt2_1 = CriarCaixaDeTexto(framet2,200,40,4,7,'Estoque:')
inputt2_1 = CriarComboBox(framet2,200,40,['Camiseta','Short','Calças','Vestidos','Acessórios'],5,7)
btnt1_2 = CriarBotão(framet2,'ENVIAR',enviar,6,7,200,40)
btnt2_2 = CriarBotão(janela,'Controle De Estoque',enviar,11,6,200,40)

produtos = []
verificacao = []
janela.mainloop()