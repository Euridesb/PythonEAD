n1 = input("Digite um número: ")
n2 = input("Digite outro número: ")

if (n1 == n2 ):
    print('Os número são iguais')
elif(n1>n2):
    print('O primeiro número é maior')
else:
    print('O segundo número é maior')
    
# else:
#     if(n1>n2):
#         print('O primeiro valor é maior que o segundo valor')
#     else:
#         print('O segundo valor é maior que o primeiro valor')
#     print('Os valores são diferentes')
print('Os valores informados são ', str(n1), 'e', str(n2))