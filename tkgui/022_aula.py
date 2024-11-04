# OBJETIVO DA AULA: trabalhar atualizar registros da base de dados
# Aula 23 com continuação
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
    # limpar as caixas de texto
    nome.delete(0, END)
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
        arquivo += f'ID: {reg[-1]}\tNome: {reg[0]}\n'
    
    arquivo_label = Label(janela, text=arquivo)
    arquivo_label.grid(row=12, column=0, columnspan=2, sticky=W)
    
    # 4. commitar as mudanças
    conn.commit()
    # 5. fechar a conexão
    conn.close() 

def save():
    # 1. criar um BD ou conectar a um
    conn = sqlite3.connect('catalogo_enderecos.db')
    # 2. criar o cursor
    cursor = conn.cursor()

    # 3. Fazer o que tem para fazer
    sql = '''UPDATE endereco SET nome = ?, sobrenome = ?, endereco = ?, cidade = ?, estado = ?, cep = ? WHERE oid = ?'''
    valores = (nome_upd.get(), sobrenome_upd.get(), endereco_upd.get(), cidade_upd.get(), estado_upd.get(), cep_upd.get(), select.get())

    cursor.execute(sql, valores)
    # 4. commitar as mudanças
    conn.commit()
    # 5. fechar a conexão
    conn.close()
    app2.destroy()

def update():
    global nome_upd, sobrenome_upd, endereco_upd, cidade_upd, estado_upd, cep_upd, app2
    app2 = Tk()
    app2.title('Atualização')
    app2.geometry('400x400')

    # 1. criar um BD ou conectar a um
    conn = sqlite3.connect('catalogo_enderecos.db')
    # 2. criar o cursor
    cursor = conn.cursor()
    # 3. Fazer o que tem para fazer
    valor = select.get()
    sql = '''SELECT * FROM endereco WHERE oid=?'''
    cursor.execute(sql, valor)
    saida = cursor.fetchall()
        
    
    nome_upd = Entry(app2, width=30)
    nome_upd.grid(row=0, column=1, padx=20, pady=(10,0))
    sobrenome_upd = Entry(app2, width=30)
    sobrenome_upd.grid(row=1, column=1)
    endereco_upd = Entry(app2, width=30)
    endereco_upd.grid(row=2, column=1)
    cidade_upd = Entry(app2, width=30)
    cidade_upd.grid(row=3, column=1)
    estado_upd = Entry(app2, width=30)
    estado_upd.grid(row=4, column=1)
    cep_upd = Entry(app2, width=30)
    cep_upd.grid(row=5, column=1)

    # criar rótulos de caixa de texto
    nome_rot_upd = Label(app2, text='Primeiro nome')
    nome_rot_upd.grid(row=0, column=0)
    sobrenome_rot_upd = Label(app2, text='Sobrenome')
    sobrenome_rot_upd.grid(row=1, column=0)
    endereco_rot_upd = Label(app2, text='Endereço')
    endereco_rot_upd.grid(row=2, column=0)
    cidade_rot_upd = Label(app2, text='Município')
    cidade_rot_upd.grid(row=3, column=0)
    estado_rot_upd = Label(app2, text='Estado')
    estado_rot_upd.grid(row=4, column=0)
    cep_rot_upd = Label(app2, text='CEP')
    cep_rot_upd.grid(row=5, column=0)
    
    # preencher caixas com resultados
    for dado in saida:
        nome_upd.insert(0, dado[0])
        sobrenome_upd.insert(0, dado[1])
        endereco_upd.insert(0, dado[2])
        cidade_upd.insert(0, dado[3])
        estado_upd.insert(0, dado[4])
        cep_upd.insert(0, dado[5])
        
    # criar o botão de salvar
    btn = Button(app2, text='Salvar', command=save)
    btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

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
    valor = select.get()
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

select = Entry(janela, width=30)
select.grid(row=7, column=1)


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

select_rot = Label(janela, text='Selecionar ID')
select_rot.grid(row=7, column=0)

# criar o botão de inserir
btn = Button(janela, text='Gravar', command=gravar)
btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

# criar apagar
btn_del = Button(janela, text='Apagar', command=apagar)
btn_del.grid(row=8,column=0, columnspan=2,padx=10, pady=10, ipadx=100)

# criar atualizar
btn_upd = Button(janela, text='Atualizar', command=update)
btn_upd.grid(row=9,column=0, columnspan=2,padx=10, pady=10, ipadx=100)

# criar pesquisar
btn_query = Button(janela, text='Pesquisa', command=query)
btn_query.grid(row=11,column=0, columnspan=2,padx=10, pady=10, ipadx=100)

janela.mainloop()
