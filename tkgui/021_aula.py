# OBJETIVO DA AULA: trabalhar apagar registros da base de dados
from tkinter import *
from PIL import Image, ImageTk
import sqlite3

janela = Tk()
janela.title('Meu App')
janela.geometry('400x400')


def gravar():
    # 1. criar um BD ou conectar a um
    conn = sqlite3.connect('catalogo_enderecos.db')
    # 2. criar o cursor
    cursor = conn.cursor()
    # 3. Fazer o que tem para fazer
    sql = '''INSERT INTO endereco (nome, sobrenome, endereco, cidade, estado, cep) VALUES (?, ?, ?, ?, ?, ?);'''
    valores = (nome.get(), sobrenome.get(), endereco.get(), cidade.get(), estado.get(), cep.get())
    cursor.execute(sql, valores)
    # 4. commitar as mudanças
    conn.commit()
    # 5. fechar a conexão
    conn.close() 
    nome.delete(0, END)     # limpar as caixas de texto
    sobrenome.delete(0, END)
    endereco.delete(0, END)
    cidade.delete(0, END)
    estado.delete(0, END)
    cep.delete(0, END)


def query():
    # 1. criar um BD ou conectar a um
    conn = sqlite3.connect('catalogo_enderecos.db')
    # 2. criar o cursor
    cursor = conn.cursor()
    # 3. Fazer o que tem para fazer
    sql = 'SELECT *, oid FROM endereco'
    cursor.execute(sql)
    saida = cursor.fetchall()
    arquivo = ''
    
    for reg in saida:
        arquivo += f'{reg[-1]}:  A pessoa se chama {reg[0]} {reg[1]} e reside na {reg[2]}, {reg[3]}/{reg[4]}, CEP {reg[5]}\n'
    
    arquivo_label = Label(janela, text=arquivo)
    arquivo_label.grid(row=10, column=0, columnspan=2)
    
    # 4. commitar as mudanças
    conn.commit()
    # 5. fechar a conexão
    conn.close()

def apagar():
    # 1. criar um BD ou conectar a um
    conn = sqlite3.connect('catalogo_enderecos.db')
    # 2. criar o cursor
    cursor = conn.cursor()
    # 3. Fazer o que tem para fazer
    sql = 'Delete from endereco WHERE oid=?'
    valor = apaga.get()
    cursor.execute(sql, valor)
   
    # 4. commitar as mudanças
    conn.commit()
    # 5. fechar a conexão
    conn.close()

  
nome = Entry(janela, width=30)
nome.grid(row=0, column=1, padx=20, pady=(10,0))
sobrenome = Entry(janela, width=30)
sobrenome.grid(row=1, column=1)
endereco = Entry(janela, width=30)
endereco.grid(row=2, column=1)
cidade = Entry(janela, width=30)
cidade.grid(row=3, column=1)
estado = Entry(janela, width=30)
estado.grid(row=4, column=1)
cep = Entry(janela, width=30)
cep.grid(row=5, column=1)

apaga = Entry(janela, width=30)
apaga.grid(row=7, column=1)


# criar rótulos de caixa de texto
nome_rot = Label(janela, text='Primeiro nome')
nome_rot.grid(row=0, column=0)
sobrenome_rot = Label(janela, text='Sobrenome')
sobrenome_rot.grid(row=1, column=0)
endereco_rot = Label(janela, text='Endereço')
endereco_rot.grid(row=2, column=0)
cidade_rot = Label(janela, text='Município')
cidade_rot.grid(row=3, column=0)
estado_rot = Label(janela, text='Estado')
estado_rot.grid(row=4, column=0)
cep_rot = Label(janela, text='CEP')
cep_rot.grid(row=5, column=0)

apaga_rot = Label(janela, text='Agapa')
apaga_rot.grid(row=7, column=0)

# criar o botão de gravar
btn = Button(janela, text='Gravar', command=gravar)
btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

# criar query
btn_query = Button(janela, text='Pesquisa', command=query)
btn_query.grid(row=9,column=0, columnspan=2,padx=10, pady=10, ipadx=100)

btn_del = Button(janela, text='Apagar', command=apagar)
btn_del.grid(row=8,column=0, columnspan=2,padx=10, pady=10, ipadx=100)

janela.mainloop()
