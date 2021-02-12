"""
Sorted

OBS: Não confunda com a função sort() que já estudamos em Listas. O sort() só funciona em listas.
Podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome diz, sorted() serve para ordenar elementos.

OBS: O sorted sempre retorna uma lista com os elementos do iterável ordenados.
"""

# Exemplo
'''
lista = [5, 2, 3]
tupla = (5, 2, 4)
conjunto = {10, 4, 1}

lista.sort()  # Só funciona para listas
print(lista)

# tupla.sort() -> Erro

# sorted() serve para qualquer iterável
tupla = sorted(tupla)
print(tupla)

lista = sorted(lista)
print(lista)

conjunto = sorted(conjunto)
print(conjunto)
'''
'''
# O sort() modifica a lista, já o sorted gera uma nova

lista = [5, 2, 3]
lista.sort()
print(lista)
print('---------')
lista = [5, 2, 3]
sorted(lista)
print(lista)
'''
'''
lista = [5, 2, 3, 7]
# Adicionando parâmetros ao sorted()

print(sorted(lista, reverse=True))  # Ordena do maior para o menor, retorna uma lista
'''

# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]
'''
print(usuarios)

# Ordenando de acordo com o nº de tweets.
print(sorted(usuarios, reverse=True, key=lambda x: len(x['tweets'])))

# Ordenando por ordem alfabetica dos usuários.
print(sorted(usuarios, key=lambda x: x['username']))
'''
# Último exemplo

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock'n roll, to young to die", "tocou": 32}
]

# Ordena da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica["tocou"], reverse=True))
