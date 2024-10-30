from tkinter import *

def btn_click(numero):
    _ = entrada.get()
    entrada.delete(0, END)
    entrada.insert(0, str(_) + str(numero))

def clear():
    entrada.delete(0, END)

def plus():
    global operation
    operation = '+'
    global number1
    number1 = float(entrada.get())
    entrada.delete(0, END)
        
def menos():
    global operation
    operation = '-'
    global number1
    number1 = float(entrada.get())
    entrada.delete(0, END)

def multiply():
    global operation
    operation = 'x'
    global number1
    number1 = float(entrada.get())
    entrada.delete(0, END)

def division():
    global operation
    operation = '/'
    global number1
    number1 = float(entrada.get())
    entrada.delete(0, END)

def result():
    number2 = float(entrada.get())
    global operation, number1
    entrada.delete(0, END)
    if operation == '+':
        resultado = number1 + number2
    elif operation == '-':
        resultado = number1 - number2
    elif operation == 'x':
        resultado = number1 * number2
    elif operation == '/':
        resultado = number1 / number2
    else:
        resultado = number2
    entrada.insert(0, str(resultado))

janela = Tk()
janela.title('Calculadora Simples')
operation = None
# Cria o widget e posiciona
entrada = Entry(janela, width=35, borderwidth=5)
entrada.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
entrada.get()

# botões
btn_7     = Button(janela, text='7',     padx=40,pady=20, command=lambda: btn_click(7)).grid(row=1, column=0)
btn_8     = Button(janela, text='8',     padx=40,pady=20, command=lambda: btn_click(8)).grid(row=1, column=1)
btn_9     = Button(janela, text='9',     padx=40,pady=20, command=lambda: btn_click(9)).grid(row=1, column=2)

btn_4     = Button(janela, text='4',     padx=40,pady=20, command=lambda: btn_click(4)).grid(row=2, column=0)
btn_5     = Button(janela, text='5',     padx=40,pady=20, command=lambda: btn_click(5)).grid(row=2, column=1)
btn_6     = Button(janela, text='6',     padx=40,pady=20, command=lambda: btn_click(6)).grid(row=2, column=2)

btn_1     = Button(janela, text='1',     padx=40,pady=20, command=lambda: btn_click(1)).grid(row=3, column=0)
btn_2     = Button(janela, text='2',     padx=40,pady=20, command=lambda: btn_click(2)).grid(row=3, column=1)
btn_3     = Button(janela, text='3',     padx=40,pady=20, command=lambda: btn_click(3)).grid(row=3, column=2)

btn_0     = Button(janela, text='0',     padx=40,pady=20, command=lambda: btn_click(0)).grid(row=4, column=0)
btn_mais  = Button(janela, text='+',     padx=39,pady=20, command=plus).grid(row=4, column=1)
btn_menos = Button(janela, text='-',     padx=40,pady=20, command=menos).grid(row=4, column=2)
btn_igual = Button(janela, text='=',     padx=39,pady=20, command=result).grid(row=5, column=0)
btn_vezes = Button(janela, text='x',     padx=40,pady=20, command=multiply).grid(row=5, column=1)
btn_div   = Button(janela, text='/',     padx=40,pady=20, command=division).grid(row=5, column=2)
btn_clear = Button(janela, text='Clear', padx=123,pady=20, command=clear).grid(row=6, column=0, columnspan=3)


janela.mainloop()