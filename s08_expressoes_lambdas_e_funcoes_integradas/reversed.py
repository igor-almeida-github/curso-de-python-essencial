"""
Reversed

OBS: Não confunda com a função reverse() que estudamos nas listas.
A Função reverse() só funciona em listas.
Já a função reversed() funciona com qualquer iterável.
Sua função é inverter o iterável.
A função reversed() retorna um iterável chamado List Reverse Iterator

"""

# Reverse - Somente para listas
'''
lista = [1, 2, 3, 4]
lista.reverse()
print(lista)
'''
# ERRO
'''
tupla = (1, 2, 3, 4)
tupla.reverse()
print(tupla)
'''
# Exemplos reversed()
'''
lista = [1, 2, 3, 4, 5]
res = reversed(lista)
print(lista)  # O reverse não altera o conteúdo da lista original.
print(type(res))
print(res)
'''
# Podemos converter o elemento retornado para uma Lista, Tupla ou Conjunto.
'''
lista = [1, 2, 3, 4, 5]
res = reversed(lista)
print(list(reversed(lista)))
print(tuple(reversed(lista)))
print(set(reversed(lista)))  # O set não definimos a ordem dos elementos
'''
# Podemos iterar sobre o reversed.
'''
for letra in reversed('Igor'):
    print(letra, end='')
'''
# Podemos fazer o mesmo sem o uso do for.
'''
print(''.join(reversed('Igor')))
'''
# Já vimos como fazer isso mais fácil com slice de strings
'''
print('Igor'[::-1])
'''
# Podemos também utilizar o reversed() para fazer um loop for reverso
'''
for n in reversed(range(0, 10)):
    print(n)
'''
# Apesar que também já vimos como fazer isso utilizando o próprio range()
'''
for n in range(9, -1, -1):
    print(n)
'''







