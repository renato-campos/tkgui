# OBJETIVO DA AULA: adicionar frames ao app - separa as partes de um app
from tkinter import *

app = Tk()
app.title('Meu aplicativo')
app.iconbitmap('tkgui/imagens/deinter6.ico')

# importante frame - quadro
frame = LabelFrame(app, text='Meu frame', padx=5, pady=5) # pad dentro da ferramento pq está na criação dela
frame.grid(row=0,column=1, padx=10, pady=10)    # pad fora da ferramenta pq está no posicionamento

# podemos criar um grid dentro do frame
btn = Button(frame, text='clique')
btn.grid(row=0, column=1)
btn1 = Button(frame, text='clique2')
btn1.grid(row=1, column=0)
# podemos ter também o frame dentro de um grid e assim por diante
btn2 = Button(app, text='clique2')
btn2.grid(row=1, column=0)

app.mainloop()