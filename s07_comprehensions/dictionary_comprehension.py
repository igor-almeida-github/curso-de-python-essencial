"""
Dictionary comprehension

Pense no seguinte:
Se quisermos criar um lista, fazemos: lista = [1, 2, 3]
Se quisermos criar uma tuplas fazemos: tupla = (1, 2, 3)
Se quisermos criar um set fazemos {1, 2, 3}
Se quisermos criar um dicionário {'a': 1, 'b': 2, 'c': 3}

# Sintaxe Dictionary comprehension
{chave: valor for chave, valor in iterável}

"""


# Exemplos:
'''
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado)
'''


# Exemplos:
'''
lista = [1, 2, 3]  # Se repetir qualquer uma das chaves, o resultado é o mesmo pois dicionário não tem chaves repetidas
quadrado = {valor: valor ** 2 for valor in lista}
print(quadrado)
'''


# Exemplos:
'''
chaves = 'abcde'
valores = [1, 2, 3, 4, 5]
mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)
'''


# Exemplo com lógica condicional

numeros = [1, 2, 3, 4, 5]

res = {num: 'par' if num % 2 == 0 else 'impar' for num in numeros}
print(res)




