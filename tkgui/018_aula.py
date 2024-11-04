# OBJETIVO DA AULA: trabalhar com drop down box
from tkinter import *
from PIL import Image, ImageTk

janela = Tk()
janela.title('Meu App')
janela.geometry('400x400')


def minha_funcao():
    pass

var = StringVar()
lista = ['A', 'B', 'C', 'D']
drop = OptionMenu(janela, var, *lista ). pack()




janela.mainloop()

print(var.get())