# OBJETIVO DA AULA: botões de seleção
from tkinter import *

def click(value):
    label = Label(app, text=value).pack()
    

app = Tk()
app.title('Meu aplicativo')
app.iconbitmap('tkgui/imagens/deinter6.ico')

var = StringVar()   # IntVar, BooleanVar
var.set('A')

# se fossem muito mais???
#Radiobutton(app, text='opção A', variable=var, value='A', command=lambda: click(var.get())).pack()
#Radiobutton(app, text='opção B', variable=var, value='B', command=lambda: click(var.get())).pack()
#Radiobutton(app, text='opção C', variable=var, value='C', command=lambda: click(var.get())).pack()
#Radiobutton(app, text='opção D', variable=var, value='D', command=lambda: click(var.get())).pack()
#Radiobutton(app, text='opção E', variable=var, value='E', command=lambda: click(var.get())).pack()

# lista de opções
lista = [
    ('opção A', 'A'),  # tupla exibido, valor
    ('opção B', 'B'),
    ('opção C', 'C'),
    ('opção D', 'D'),
    ('opção E', 'E')
]

for tupla in lista:
    Radiobutton(app, text=tupla[0], variable=var, value=tupla[1], command=var.get()).pack(anchor=W)

#label = Label(app, text=var.get()).pack()

btn = Button(app, text='Clique!', command=lambda: click(var.get())).pack()

app.mainloop()