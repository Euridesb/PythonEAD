class Veiculo:  
    # Atributos -> caracteristicas da Classe.
    # cor = 'Preto'
    # ano = 2021
    # porta = 4
    modelo = 'X6'
    # Medoto construtor.
    def __init__(self,cor,ano,porta):
        self.cor = cor
        self.ano = ano
        self.porta = porta
        
    # Medotos -> Acões da Classe. 
    def acelerar(self,velocidade):
        print('Acelerou a',velocidade,'Km/h')
    def Frear(self):
        print('Freou')