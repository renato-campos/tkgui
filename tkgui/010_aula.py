# OBJETIVO DA AULA: criar uma barra de status
from tkinter import *
from PIL import Image, ImageTk


def backward(image_number):
    global label
    global btn_frente
    global btn_voltar
    label.grid_forget()
    label = Label(image=lista_imagens[image_number-1])
    btn_voltar = Button(
        app, text='<<', command=lambda: backward(image_number-1))
    btn_frente = Button(
        app, text='>>', command=lambda: forward(image_number+1))

    if image_number == 1:
        btn_voltar = Button(app, text='<<', state='disabled')

    label.grid(row=0, column=0, columnspan=3)
    btn_voltar.grid(row=1, column=0)
    btn_frente.grid(row=1, column=2)
    
    status = Label(app, text=f'Imagem {image_number} de {len(lista_imagens)}',  # importante
               bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2,column=0,columnspan=3, sticky='WE')


def forward(image_number):
    global label
    global btn_frente
    global btn_voltar
    label.grid_forget()
    label = Label(image=lista_imagens[image_number-1])
    btn_voltar = Button(
        app, text='<<', command=lambda: backward(image_number-1))
    btn_frente = Button(
        app, text='>>', command=lambda: forward(image_number+1))

    if image_number == 5:
        btn_frente = Button(app, text='>>', state='disabled')

    label.grid(row=0, column=0, columnspan=3)
    btn_voltar.grid(row=1, column=0)
    btn_frente.grid(row=1, column=2)
    
    status = Label(app, text=f'Imagem {image_number} de {len(lista_imagens)}',  # importante
               bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2,column=0,columnspan=3, sticky='WE')


app = Tk()
app.title('Meu aplicativo')
app.iconbitmap('tkgui/imagens/deinter6.ico')

imagem1 = ImageTk.PhotoImage(Image.open('tkgui/imagens/1.png'))
imagem2 = ImageTk.PhotoImage(Image.open('tkgui/imagens/2.png'))
imagem3 = ImageTk.PhotoImage(Image.open('tkgui/imagens/3.png'))
imagem4 = ImageTk.PhotoImage(Image.open('tkgui/imagens/4.png'))
imagem5 = ImageTk.PhotoImage(Image.open('tkgui/imagens/5.png'))

lista_imagens = [imagem1, imagem2, imagem3, imagem4, imagem5]

status = Label(app, text=f'Imagem 1 de {len(lista_imagens)}',        # importante
               bd=1, relief=SUNKEN, anchor=E)

label = Label(image=imagem1)
label.grid(row=0, column=0, columnspan=3)

btn_voltar = Button(app, text='<<', command=backward, state='disabled')
btn_sair = Button(app, text='Sair do programa', command=app.quit)
btn_frente = Button(app, text='>>', command=lambda: forward(2))

btn_voltar.grid(row=1, column=0)
btn_sair.grid(row=1, column=1)
btn_frente.grid(row=1, column=2, pady=10)
status.grid(row=2,column=0,columnspan=3, sticky='WE')                # importante

app.mainloop()
