import sqlite3
from sqlite3 import Error
from tkinter import messagebox

# Criando uma concexão com o banco
def conexao():
    conn = None
    try:
        conn = sqlite3.connect('user.db')
    except Error as e:
        print(e)
    return conn

vcon = conexao()

# essa função tem por objetivo apenas salvar os dados no banco
def salvar(conexao, query):
    try:
        c = conexao.cursor()
        c.execute(query)
        conexao.commit()
    except Error:
        messagebox.showwarning(title='aviso', message='este usuário ja existe, tente outro')

# buscar todos os usuários do banco

bquery = """
    select usuario, senha from pessoas
"""

def buscar(conexao, query):
    c = conexao.cursor()
    c.execute(query)
    consulta = c.fetchall()
    return consulta
