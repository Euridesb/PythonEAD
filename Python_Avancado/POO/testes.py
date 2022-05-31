

def comparaValores(v1,v2):
    if(v1!=v2):
        v1=v2
    assert(v1==v2)

def ObtemEscola(escola):
    if(escola!='Proway'):
        escola = 'Proway'
    assert(escola == 'Proway')

def ValidaIdade(ano):
    idade = 2022 - ano
    assert(idade >=18)

def ValidaSoma(v1,v2):
    soma = v1 + v2
    assert(soma>=10)

ValidaSoma(5,3)
ValidaIdade(2002)
ObtemEscola('Nome da escola')
comparaValores(30,25)