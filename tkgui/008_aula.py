# OBJETIVO DA AULA: inserção de uma imagem na janela e
# "favicon" na barra de título do tkinter 
from tkinter import *
from PIL import Image, ImageTk


app = Tk()
app.title('Meu aplicativo')
app.iconbitmap('tkgui/imagens/deinter6.ico')    # favicon

imagem1 = ImageTk.PhotoImage(Image.open('tkgui/imagens/4.png')) # imagem
label = Label(image=imagem1)
label.pack()

btn_sair = Button(app, text='Sair do programa', command=app.quit)
btn_sair.pack()
app.mainloop()