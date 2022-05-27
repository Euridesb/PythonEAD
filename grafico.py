import matplotlib.pyplot as grafico
nota = [8,9,10,6]
bim  = ['Primeiro','Segundo','Terceiro','Quarto']

# matplotlib.pyplot.title('Notas Bimestrais')
# matplotlib.pyplot.plot(bim,nota)

# matplotlib.pyplot.show()

grafico.title('Notas Bimestrais.')
grafico.plot(bim,nota)
grafico.show()