# OBJETIVO DA AULA: trabalhar com check box
from tkinter import *
from PIL import Image, ImageTk

janela = Tk()
janela.title('Meu App')
janela.geometry('400x400')


def minha_funcao():
    label = Label(janela, text=variavel.get()).pack()


# variavel = IntVar()
variavel = StringVar(value=OFF)


# cbx = Checkbutton(janela, text='opção', variable=variavel).pack()
cbx = Checkbutton(janela, text='opção', variable=variavel,
                  onvalue='ligado', offvalue='desligado').pack()
btn = Button(janela, text='Pegar Valor', command=minha_funcao).pack()

janela.mainloop()

print(variavel.get())

'''
IntVar = automático 0 ou 1
StringVar = precisa determinar onvalue / offvalue / empty state => value=OFF
'''
