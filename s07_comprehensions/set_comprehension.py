"""
Set_Comprehension


"""

# Exemplo 1:
'''
numeros = {num for num in range(1, 7)}
print(numeros)
'''


# Exemplo 2:
'''
impares = {num for num in range(1, 20) if num % 2}
print(impares)
'''


# Exemplo 3:
'''
numeros = {x ** 2 for x in range(10)}
print(numeros)
'''


# Exemplo 4: (Em um conjunto não existe repetição nem ordenação)
letras = {letra for letra in 'aaaaaaaaaaaaaaaaaaaaahhh'}
print(letras)  # resultado {'h', 'a'}

