# OBJETIVO DA AULA: CRIAR NOVAS JANELAS
from tkinter import *
from PIL import Image, ImageTk

def open():
    app2 = Toplevel()   # abre outra janela
    label2 = Label(app2, text='minha janela 2').pack()
    btn2 = Button(app2, text='fechar', command=app2.destroy).pack()
    # se tentar incluir algo e não aparecer, tente colocar como variavel global
    
    
app = Tk()
app.geometry('300x450')
app.title('Meu aplicativo')
app.iconbitmap('tkgui/imagens/deinter6.ico')    

label = Label(app, text='minha janela 1').pack()
btn1 = Button(app, text='abre a janela 2', command=open).pack()

app.mainloop()