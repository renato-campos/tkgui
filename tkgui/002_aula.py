# OBJETIVO DA AULA: posicionar as ferramentas através do grid
from tkinter import *

janela = Tk()

# Cria o widget e posiciona
label = Label(janela, text='Olá Mundo!')
label2 = Label(janela, text='Tchau mundo.!')
# construção e posicionamento ao mesmo tempo POO
label3 = Label(janela, text='Até a próxima!').grid(row=2,column=1)
# cria uma matriz de posicionamento, ignora colunas e linhas vazias
label.grid(row=0,column=2)
label2.grid(row=1,column=0)

janela.mainloop()