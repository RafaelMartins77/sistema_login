import conexaobd as bd
from tkinter import *
from tkinter import  messagebox

# essa função tem por objetivo salvar novos usuários no banco


def save(user, password):
    vquery = f"""
        insert into pessoas (usuario, senha)
        values('{user}', '{password}')
    """
    bd.salvar(bd.vcon, vquery)

# essa função faz o login e altera o estado de login


def login(user, password):
    data = bd.buscar(bd.vcon, bd.bquery)
    res = None
    for us, pas in data:
        if (user, password) == (us, pas):
            res = True
            break
        else:
            res = False
    return res


def sair(troca):
    troca['text'] = 'não logado'
    troca['background'] = '#F0E68C'


def estadologin(nome, senha, var):
    if (nome.get() and senha.get()) == "":
        messagebox.showwarning(title='Aviso', message='você precisa preencher ambos os campos')
    else:
        loged = login(nome.get(), senha.get())
        if loged:
            var['text'] = 'usuário logado'
            var['background'] = '#98FB98'
        else:
            var['text'] = 'usuário ou senha inválidos'
            var['background'] = '#FFC0CB'
        senha.delete(0, END)
