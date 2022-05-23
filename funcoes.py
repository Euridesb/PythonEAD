# Aqui é as funções
# def mensagen():
#     print('Olá Mundo')

# def calcula():
#     print(2+2)

# def defineNome(pNome):
#     print('O nome informado foi:',pNome)

# def Escola(pEscola):
#     print('Você esta estudado na escola:',pEscola)

def Escola2(pEscola = 'Escola2'):
    print('Você esta estudado na escola:',pEscola)

# def SomaValores(pValor1, pValor2):
#     print(pValor1 + pValor2)
    
# Aqui é o corpo do programa
# mensagen()
# calcula()
# defineNome('Eurides')
# Escola('Prowey')
Escola2()

# valor1 = int(input('Digite um valor:'))
# valor2 = int(input('Digite outro valor:'))
# SomaValores(valor1, valor2)


def ValidaAcesso(usuario):
    if(usuario == 'Prowey'):
        print('Login efetuado com sucesso')
    else:
        print('Login Inválido.')