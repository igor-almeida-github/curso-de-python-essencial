"""
List Comprehension

- Utilizando List Comprehension nós podemos gerar novas lista com dados processados a partir de outro iterável.

# Sintaxe da List Comprehension

[ dado for dado in iterável ]

"""


# Exemplos
'''
numeros = [2, 4, 6, 8, 10]
res = [2 * num for num in range(1, 6)]
print(res)
res = [num for num in numeros]
print(res)


def funcao(num):
    return num ** 2


print([funcao(num) for num in numeros])
'''


# List comprehension vs loop
'''
# loop

lista = []
for i in range(1, 11):
    lista.append(i ** 2)
print(lista)


# List comprehension

lista = [i ** 2 for i in range(1, 11)]
print(lista)
'''


# Outros exemplos:

# 1
'''
nome = 'Igor Almeida'

print([letra.upper() for letra in nome])

# 2

amigos = ['naruto', 'sakura', 'gara', 'hinata']

print([amigo.replace(amigo[0], amigo[0].upper()) for amigo in amigos])
'''


# Nós podemos adicionar estruturas condicionais lógicas as nossas list comprehensions

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = [num for num in numeros if not num % 2]
print(pares)

print([num * 2 if num % 2 == 0 else num / 2 for num in numeros])




