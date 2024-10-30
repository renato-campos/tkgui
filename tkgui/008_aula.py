from tkinter import *
from PIL import Image, ImageTk


app = Tk()
app.title('Meu aplicativo')
app.iconbitmap('tkgui/imagens/deinter6.ico')

imagem1 = ImageTk.PhotoImage(Image.open('tkgui/imagens/cecop2.png'))
label = Label(image=imagem1)
label.pack()

btn_sair = Button(app, text='Sair do programa', command=app.quit)
btn_sair.pack()
app.mainloop()