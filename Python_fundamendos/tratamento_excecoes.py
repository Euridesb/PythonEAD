# try:
#     print(2/0)
# except:
#     print('Erro: Exceção Gerada.')


# try:
#     print(2/0)
# except ZeroDivisionError as erro:
#     print('Impossivel dividir por zero [' +str(erro) +']')
# except NameError as mensagem:
#     print('Variavel não declarada [' + str(mensagem) + ']')
# finally:
#     print('Operação efetuada com sucesso.')

try:
    print('Carregando Operação')
    y = 0
    for x in range(0,632):
        y = y + 1
finally:
    print('Operação finalizada com sucesso')