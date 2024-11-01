# OBJETIVO DA AULA: usar a caixa de diálogo de abertura de arquivos
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from pathlib import Path

app = Tk()
app.geometry('300x450')
app.title('Meu aplicativo')
app.iconbitmap('tkgui/imagens/deinter6.ico')


def open(janela, caminho):
    global imagem
    # como abrir a caixa de diálogo - o comando apenas retorna o caminho e você trata como quiser
    janela.filename = filedialog.askopenfilename(initialdir=caminho, title='Buscar boletins de ocorrências', filetypes=(('todos', '*.*'), ('excel files', '*.xlsx'), ('pdf files', '*.pdf')))
    imagem = ImageTk.PhotoImage(Image.open(janela.filename))
    label = Label(janela, text=janela.filename).pack()
    label2 = Label(janela, image=imagem).pack()


endereco_inicial = Path.home() / 'Downloads'
btn = Button(app, text='Abrir arquivo',
             command=lambda: open(app, endereco_inicial)).pack()

app.mainloop()
