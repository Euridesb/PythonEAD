# texto = list()
# criando um arquivo e escrevendo
# arq = open('arquivo.txt', 'a')
# # arq.write('\nde novo uma nova linha.')
# texto.append('Conteudo da primeira linha')
# texto.append('\nConteudo da segunda linha.')
# texto.append('\nConteudo da Terceira Linha.')
# arq.writelines(texto)
# arq.close()


arq = open('arquivo.txt','r')
total = 0
# print(arq.readlines())
# print(arq.readlines())
# print(arq.readlines())
for linha in arq:
    # retona as informações em forma de lista
    # linha = linha.rsplit()

    linha = linha.rstrip()
    print(linha)
    total = total + 1
print(''.ljust(30,'-'))
print('Leitura efetuada com Sucesso.')
print('Total de linhas:',total)
arq.close()