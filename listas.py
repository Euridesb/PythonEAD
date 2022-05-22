  #   |     0    |    1     |    2    |  3  |  4 |
lista = ['Mouse', 'Teclado', 'Monitor',  50,  2.0]
print('O Item na posição 1 é',lista[0])
print(type(lista[2]))

# Adiciona em qualquer posição da Lista 
lista.insert(3,'Processador')
print(lista[3])

# Adiciona ao final da Lista
lista.append('Placa Mãe')
print(lista[6])

# Remover intem da Lista
lista.pop(4)
print(lista)

# Remover item pela nomenclatura
lista.remove('Mouse')
print(lista)