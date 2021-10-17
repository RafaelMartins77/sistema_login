import conexaobd as bd
from tkinter import *

# essa função tem por objetivo salvar novos usuários no banco
def save(user, password):
    vquery = f"""
        insert into pessoas (usuario, senha)
        values('{user}', '{password}')
    """
    bd.salvar(bd.vcon, vquery)

def login(user, password, sta):
    data = bd.buscar(bd.vcon, bd.bquery)
    loged = False
    for us, pas in data:
        if (user.get(), password.get()) == (us, pas):
            loged = True
            break
        else:
            loged = False
    if loged:
        mudastatus(sta)
    else:
        senhaerro(sta)
    password.delete(0, END)

def mudastatus(troca):
    troca['text']= 'usuário logado'
    troca['background']= '#98FB98'

def senhaerro(troca):
    troca['text'] = 'usuário ou senha inválidos'
    troca['background'] = '#FFC0CB'

def sair(troca):
    troca['text'] = 'não logado'
    troca['background'] = '#F0E68C'
