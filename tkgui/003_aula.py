# OBJETIVO DA AULA: formatações dos botões
from tkinter import *

janela = Tk()

def minha_funcao():
    label = Label(janela, text='Cliquei no botão!!')
    label.pack()

# Cria o widget e posiciona
btn = Button(janela, text='Click', state='disabled')
btn.pack()
btn2 = Button(janela, text='Click', padx=150, command=minha_funcao) # o pad dimensiona largura do botão
btn2.pack()
btn3 = Button(janela, text='Click', pady=25, fg='red', bg='green') # altura do botão
btn3.pack()

janela.mainloop()