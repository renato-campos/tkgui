# OBJETIVO DA AULA: criar uma janela do aplicativo e inserir rótulo
from tkinter import *

janela = Tk()

# Cria o widget e posiciona
label = Label(janela, text='Olá Mundo!')
label.pack()

janela.mainloop()