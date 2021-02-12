"""
Min e Max

max() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elementos.
min() -> Retorna o menor valor em um iterável ou o menor de dois ou mais elementos.
"""
# Exemplos max()
'''
lista = [1, 8, 4, 99, 129]
print(max(lista))  # 129

tupla = (1, 8, 4, 99, 129)
print(max(tupla))  # 129

conjunto = {1, 8, 4, 99, 129}
print(max(conjunto))  # 129
'''
'''
dicionario = {'a': 1, 'b': 8, 'c': 40, 'd': 30, 'e': 20}
print(max(dicionario))  # e (olha quem é o maior pela chave e retorna a chave)
print(max(dicionario, key=lambda x: dicionario[x]))  # c (Olha quem é o maior pelo valor e retorna a chave)
print(max(dicionario.values()))  # 40 (Olha quem é o maior pelo valor e retorna o valor)
print(max(1, 2.44, -3, 4))  # 4
print(max('a', 'c', 'b'))  # c
print(max('abelha', 'cachorro', 'gato'))  # gato (ordem alfabética)
print(max('aaaaa', 'aa', 'a'))  # aaaaa
print(max('abcde'))  # 'e'
'''
'''
# Faça um programa que pega dois valores do usuário e mostre o maior (keep it simple)
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))
print(f'O maior valor é: {max(val1, val2)}')
'''

# Exemplos max()
'''
lista = [1, 8, 4, 99, 129]
print(min(lista))  # 1

tupla = (1, 8, 4, 99, 129)
print(min(tupla))  # 1

conjunto = {1, 8, 4, 99, 129}
print(min(conjunto))  # 1
'''
'''
dicionario = {'a': 1, 'b': 0, 'c': 40, 'd': 30, 'e': 20}
print(min(dicionario))  # a (olha quem é o menor pela chave e retorna a chave)
print(min(dicionario, key=lambda x: dicionario[x]))  # b (Olha quem é o menor pelo valor e retorna a chave)
print(min(dicionario.values()))  # 0 (Olha quem é o menor pelo valor e retorna o valor)
print(min(1, 2.44, -3, 4))  # -3
print(min('a', 'c', 'b'))  # a
print(min('abelha', 'cachorro', 'gato'))  # abelha (ordem alfabética)
print(min('aaaaa', 'aa', 'a'))  # a
print(min('abcde'))  # 'a'
'''
'''
# Faça um programa que reba dois valores do usuário e mostre o menor (keep it simple)
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))
print(f'O menor valor é: {min(val1, val2)}')
'''
# Outros exemplos
'''
nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']
print(max(nomes, key=len))  # Ollivander
print(min(nomes, key=len))  # Tim
'''
'''
musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock'n roll, to young to die", "tocou": 32}
]

print(max(musicas, key=lambda musica: musica["tocou"]))  # A mais tocada
print(min(musicas, key=lambda musica: musica["tocou"]))  # A menos tocada

# DESAFIO! Imprima somente o título do música mais e menos tocada
print(max(musicas, key=lambda musica: musica["tocou"])['titulo'])  # A mais tocada
print(min(musicas, key=lambda musica: musica["tocou"])['titulo'])  # A menos tocada

# DESAFIO! Como encontrar a música mais tocada e a menos tocada sem usar max(), min() e lambda?
print(sorted(musicas, key=lambda musica: musica["tocou"])[-1]["titulo"])  # A mais tocada
print(sorted(musicas, key=lambda musica: musica["tocou"])[0]["titulo"])  # A menos tocada
'''