# OBJETIVO DA AULA: criando caixas de mensagens
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox


app = Tk()
app.title('Meu aplicativo')
app.iconbitmap('tkgui/imagens/deinter6.ico')

# tipos de caixa de mensagens:
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    #response = messagebox.showinfo('Esse é o título', 'Essa é a mensagem')                #ok
    #response = messagebox.showwarning('Esse é o título', 'Esse é o alerta')               #ok
    #response = messagebox.showerror('Esse é o título', 'Esse é o erro')                   #ok
    #response = messagebox.askquestion('Esse é o título', 'Essa é a pergunta?')  #yes/no
    #response = messagebox.askokcancel('Esse é o título', 'Quer cancelar?')     #0/1
    response = messagebox.askyesno('Esse é o título', 'Essa é a pergunta?')    #0/1
    Label(app, text=response).pack()    # serve para mostrar qual o retorno das caixas de msg 0/1
    #if response:    # trata a resposta
    #    Label(app, text='Aceitou').pack()
    #else:
    #    Label(app, text='Recusou').pack()


Button(app, text='Popup',command=popup).pack()


app.mainloop()