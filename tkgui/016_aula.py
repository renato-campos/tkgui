# OBJETIVO DA AULA: barras de rolagem
from tkinter import *


def slide(var):
    global label
    # o slider retorna um número e você trata com o get
    label = Label(app, text=vertical.get()).pack()
    app.geometry(f'400x{vertical.get()}')


app = Tk()
app.geometry('300x450')
app.title('Meu aplicativo')
app.iconbitmap('tkgui/imagens/deinter6.ico')

vertical = Scale(app, from_=200, to=400, command=slide)
vertical.pack()     # precisa fazer o posicionamento separado

horizontal = Scale(app, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()     # precisa fazer o posicionamento separado


# btn = Button(app, text='clique', command=slide).pack()

app.mainloop()
