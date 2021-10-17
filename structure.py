import conexaobd as bd

# essa função tem por objetivo salvar novos usuários no banco
def save(user, password):
    vquery = f"""
        insert into pessoas (usuario, senha)
        values('{user}', '{password}')
    """
    bd.salvar(bd.vcon, vquery)


def login(user, password):
    data = bd.buscar(bd.vcon, bd.bquery)
    for us, pas in data:
        if (user, password) == (us, pas):
            print('usuário logado')
            pass
        else:
            print('sinto muito')