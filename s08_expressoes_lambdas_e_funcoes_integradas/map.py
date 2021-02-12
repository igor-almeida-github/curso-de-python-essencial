"""
Map
Com map, fazemos mapeamento de valores para função.
"""

import math


def area(r):
    """Calcula a área de um cículo com raio 'r'."""
    return math.pi * (r ** 2)


raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum
'''
areas = []
for r in raios:
    areas.append(area(r))

print(areas)
'''

# Forma 2 - Map é uma função que recebe dois parâmetros: o primeiro é a função e o segundo, um iterável
'''
areas = []
areas = map(area, raios)
print(areas)
print(type(areas))
print(list(areas))
'''

# OBS: Após utilizar a função map(), depois da primeira utilização do resultado, ele se torna vazio
'''
areas = map(area, raios)
print(list(areas))
print(list(areas))  # Vazio
areas = map(area, raios)
for i in areas:
    print(i)
for i in areas:
    print(i)
'''

# Forma 3 - Map com Lambda
'''
print(list(map(lambda r: math.pi * (r ** 2), raios)))
'''

# Para fixar map
# Temos dados iteráveis:
# Dados: a1, a2, ..., an
# Temos uma função:
# Função: f(x)
# Utilizamos a função map(f, dados) onde map irá 'mapear'cada elemeto dos dados e aplicar a função.
# O map object: f(a1), f(a2), ..., f(an)

# Mais um exemplo (mostrando temperatura em farenheit)
cidades = [('Belim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27)]
print(cidades)
print(list(map(lambda dado: (dado[0], dado[1] * 9/5 + 32), cidades)))

