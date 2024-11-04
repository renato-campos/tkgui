# OBJETIVO DA AULA: trabalhar criando a bases de dados
from tkinter import *
from PIL import Image, ImageTk
import sqlite3

janela = Tk()
janela.title('Meu App')
janela.geometry('400x400')


def minha_funcao():
    pass

# databases
# 1. criar um BD ou conectar a um
conn = sqlite3.connect('catalogo_enderecos.db')
# 2. criar o cursor
cursor = conn.cursor()

# 2.1. criar a tabela SQLite tipos(text, integer, real, None, blob)
sql = '''CREATE TABLE endereco(
    nome text,
    sobrenome text,
    endereco text,
    cidade text,
    estado text,
    cep integer
)
'''     # só roda um vez
cursor.execute(sql)



# 3. commitar as mudanças
conn.commit()
# 4. fechar a conexão
conn.close()



janela.mainloop()