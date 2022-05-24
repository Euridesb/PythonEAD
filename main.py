import funcoes
# usuario = input('Informe o nome de usuario para acessar o sistema:')

# funcoes.ValidaAcesso(usuario)

# funcoes.Escola2()
usuario = input('Usuario:')

senha = input('Senha: ')

funcoes.ValidaAcesso(usuario, senha)
# print('O sistema continua.')
funcoes.MostraMenuPrincipal()