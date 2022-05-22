  #   |     0    |    1     |    2    |  3  |  4 |
# lista = ['Mouse', 'Teclado', 'Monitor',  50,  '2.0']
# print('O Item na posição 1 é',lista[0])
# print(type(lista[2]))

# Adiciona em qualquer posição da Lista 
# lista.insert(3,'Processador')
# print(lista[3])

# # Adiciona ao final da Lista
# lista.append('Placa Mãe')
# print(lista[6])

# Remover intem da Lista
# lista.pop(4)
# print(lista)

# # Remover item pela nomenclatura
# lista.remove('Mouse')
# print(lista)

# print(len(lista))

# print(lista)

# for x in range(0,len(lista)):
#   if( 2.0 == lista[x]):
#     lista.remove(2.0)
#     break
# print(lista)

# existe = False
# produto = input('Qual o produto deseja excluir da lista? ')

# for x in range(0,len(lista)):
#   if(produto.upper() == lista[x].upper()):
#     lista.pop(x)
#     existe = True
#     break
# print(lista)

# if(existe):
#   print(produto, 'Foi excluido da lista')
# else:
#   print(produto, 'não existe na lista')

# print(lista)

# lista.sort()

# print(lista)

# lista.reverse()
# print(lista)

# print(len(lista))

# lista = ['Mouse', 'Teclado', 'Monitor',  50,  '2.0']
# print(type(lista))

# tupla = tuple('ABCD')
# for x in range(0,len(tupla)):
#   print(x,'=', tupla[x])
# print(type(tupla))
# print(tupla[2])
# print(tupla)

# dias_semana = ('Domingo', 'Segunda','Terça','Quarta','Quinta','Sexta','Sabado')
# print(dias_semana)

# for x in range( len( dias_semana)):   
#   if(dias_semana[x] == 'Domingo'):
#     print(str(x+1), '= Domigo')
#   elif(dias_semana[x]== 'Segunda'):
#     print(str(x+1),'= Segunda-Feira')
#   elif(dias_semana[x] == 'Terça'):
#     print(str(x+1),'= Terça-Feira')
#   elif(dias_semana[x] == 'Quarta'):
#     print(str(x+1),'= Quarta-Feira')
#   elif(dias_semana[x] == 'Quinta'):
#     print(str(x+1),'= Quinta-Feira')
#   elif(dias_semana[x] == 'Sexta'):
#     print(str(x+1),'= Sexta-Feira')
#   else:
#     print(str(x+1),'= Sábado')

# Execício

existe = False
dias_semana = ('Domingo', 'Segunda','Terça','Quarta','Quinta','Sexta','Sabado')
Inf_dia = input('Informe o dia da semana: ')
for x in range(0,len(dias_semana)):
  if(dias_semana[x].upper()==Inf_dia.upper()):
    existe = True
    break

if ( existe):
  print(dias_semana[x], 'fica na posiçao ', x)
else:
  print('Dia da semana inválido')  