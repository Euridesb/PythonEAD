
# => Super Classe
class Veiculo:  
    # Atributos -> caracteristicas da Classe.
    # cor = 'Preto'
    # ano = 2021
    # porta = 4
    modelo = 'X6'
    
    # Medoto construtor 
    def __init__(self,cor,ano,porta,marca):
        self.cor = cor
        self.ano = ano
        self.porta = porta
        print('Eu sou médoto construtor da Super Classe',marca,__class__.__name__)
        
    # Medotos -> Acões da Classe. 
    def acelerar(self,velocidade):
        print('Acelerou a',velocidade,'Km/h')
    def Frear(self):
        print('Freou')

    @classmethod
    def metodo_de_classe(cls,parametro1,parametro2):
        print('Eu sou um metodo de classe')
        print(f'Valor do parametro 01: {parametro1}')
        print(f'Valor do parametro 02: {parametro2}')


# Classe Herdeira. 
class Carro(Veiculo):
    #Método construtor da Classe Herdeira.
    def __init__(self,modelo):
        print('Eu sou o Construtor da Classe Herdeira',modelo,__class__.__name__)
    
    def ObtemModelo(self):
        print('Eu sou o modelo do carro')