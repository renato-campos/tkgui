# OBJETIVO DA AULA: trabalhar com entrada de texto
from tkinter import *

janela = Tk()

def minha_funcao():
    label = Label(janela, text='Olá ' + entrada.get())
    label.pack()

# Cria o widget e posiciona
entrada = Entry(janela, width=50, bg='gray', fg='white', borderwidth=3)
entrada.pack()
entrada.insert(0, 'Digite seu nome:')
entrada.get()

btn = Button(janela, text='Clique', command=minha_funcao)
btn.pack()

janela.mainloop()