# Aqui é as funções
# def mensagen():
#     print('Olá Mundo')

# def calcula():
#     print(2+2)

# def defineNome(pNome):
#     print('O nome informado foi:',pNome)

# def Escola(pEscola):
#     print('Você esta estudado na escola:',pEscola)

# def Escola2(pEscola = 'Escola2'):
#     print('Você esta estudado na escola:',pEscola)

# def SomaValores(pValor1, pValor2):
#     print(pValor1 + pValor2)
    
# Aqui é o corpo do programa
# mensagen()
# calcula()
# defineNome('Eurides')
# Escola('Prowey')
# Escola2()

# valor1 = int(input('Digite um valor:'))
# valor2 = int(input('Digite outro valor:'))
# SomaValores(valor1, valor2)


# def ValidaAcesso(usuario):
#     if(usuario == 'Prowey'):
#         print('Login efetuado com sucesso')
#     else:
#         print('Login Inválido.')
produto = []
nome =''
novoNome=''
def ValidaAcesso(pUsuario, pSenha):
    # if((pUsuario == 'Aluno') and (pSenha == 'Proway')):
    #     print('Login efetuado com Sucesso')
    # else:
    #     print('Login ou senha Invalido')
    while((pUsuario != 'Aluno') or (pSenha != 'Proway')):
        print('Usuario/Senha Invalido.')
        pUsuario = input('Usuario:')
        pSenha = input('Senha:')
    
def MostraMenuPrincipal():
    opcao = 0
    while(opcao != 5):
        print('+'.ljust(34,'-')+'+')
        print('| 1 - Cadastrar | 2 - Alterar     |')
        print('| 3 - Excluir   | 4 - Visualizar  |')
        print('|           5 - Sair              |')
        print('+'.ljust(34,'-')+'+')
        opcao = int(input('Opção desejada:'))
        if(opcao == 1):
            nome = input('Nome do prduto desejado: ')
            if(nome in produto):
                print(nome,'Já esta cadastrado.')
            else:
                produto.append(nome)
                print(nome,'Cadastrado com sucesso.')
        elif(opcao == 2):
            nome = input('Nome do produto que deseja alterar:')
            if(nome in produto):
                for x in range(0,len(produto)):
                    if(produto[x]==nome):
                        novoNome = input('Informe novo nome para ' + nome + ' ')
                        produto[x]=novoNome
                        break
            else:
                print(nome,'Não esta cadastrado.')   
        elif(opcao == 3):
            nome = input('Qual o produto que deseja excluir: ')
            if (nome in produto):
                produto.remove(nome)
                print(nome,' excluido com Sucesso.')
            else:
                print(nome,'não esta cadastrado.')
        elif(opcao == 4):
            # Visualizar
            if(len(produto) == 0):
                print('Não tem produto cadastrado.')
            else:
                print(produto)
        elif(opcao == 5):
            # Sair
            print('Obrigado por usar o nosso sistema')
        else:
            print('Opação Invalida')