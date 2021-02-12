"""
Zip

zip() -> Cria um iterável (Zip Object) que agrega elementos de cada um dos iteráveis passados como entrada em pares.

"""

# Exemplos
'''
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)

print(zip1)
print(type(zip1))

# Sempre podemos gerar uma Lista, Tupla, Set ou Dicionário

print(list(zip(lista1, lista2, 'abc')))
print(tuple(zip(lista1, lista2)))
print(set(zip(lista1, lista2)))
print(dict(zip(lista1, lista2)))
'''
# OBS: O zip() utiliza como parâmetro o menor tamanho em iterável. Isso significa que se estiver
# trabalhando com iteráveis de tamanhos diferentes, irá parar quando os elementos do menor iterável acabar:
'''
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [7, 8, 9, 10, 11]

zip1 = zip(lista1, lista2, lista3)
print(list(zip1))
'''
# Podemos utilizar diferentes iteráveis com o zip
'''
tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}
zt = zip(tupla, lista, dicionario.values())
print(list(zt))
'''
# Lista de tuplas
'''
dados = [(0, 1), (1, 2), (2, 3), (3, 4)]
print(list(zip(*dados)))
'''
# Exemplos mais complexos
'''
prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['Maria', 'Pedro', 'Carla']
final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}  # Maior nota de cada aluno
print(final)
'''
# Podemos utilizar o map()
'''
prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['Maria', 'Pedro', 'Carla']
final = zip(alunos, map(max, zip(prova1, prova2)))
print(dict(final))
'''
