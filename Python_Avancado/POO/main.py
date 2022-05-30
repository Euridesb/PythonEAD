from classe import Veiculo, Carro


v1 = Veiculo('Preto',2021,4,'volksvagem')

# print(v1.cor)
# print(v1.porta)
v1.acelerar(30)
v1.Frear()
print(v1.cor)
print(v1.ano)
print(v1.porta)
print(v1.modelo)

Veiculo.metodo_de_classe(parametro1=20,parametro2=50)

v2 = Carro('gol')
v2.ObtemModelo()