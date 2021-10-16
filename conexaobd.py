import sqlite3
from sqlite3 import Error

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
        c.excute(query)
        conexao.commit()
    except Error as e:
        print(e)

# buscar todos os usuários do banco
def buscar(conexao, query):
    c = conexao.cursor()
    c.excute(query)
    consulta = c.fetchall()
    return consulta
