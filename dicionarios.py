# lista = [1,2,3]
# tupla = (1,2,3)
# print(type(lista))
# print(type(tupla))

# dicionario = {1,2,3}
# print(type(dicionario))

       #P1 V1  P2  V2  P3   V3
# num = {1:'one', 2:'two',3:'three'}
# num[4] = 'four'
# num[5] = 'five'
# del num[5]
# print(num)
# indice = int(input('Qual posição que deseja excluir: '))

# print(num.pop(indice, 'Posição Inexistente.'))
# print(num)

# valor = int(input('Digite uma posição: '))
# if(num.get(valor) == None ):
#     print('Valor Inexistente.')
# else:
#     print(num.get(valor))
# print(len(num))

num = {1:'one', 2:'two',3:'three'}
num2 = {4:'four',5:'five',6:'six'}   
num.update(num2)
print(num)
print(num[6])