"""
Listas Aninhadas (Nested Lists)

- Algumas linguagens de programação (C/Java) possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais (Array/Vetores);
    - Multidimensionais (Matrizes);

Em Python temos as listas
numeros = [1, 2, 3, 4]

"""


# Exemplos
'''
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3x3
print(matriz)
print(type(matriz))


# Como fazemos para acessar os dados?

print(matriz[0])
print(matriz[1])
print(matriz[1][1])
'''

# Iterando com loops em lista aninhada
'''
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3x3
for lista in matriz:
    print(lista)

for lista in matriz:
    for num in lista:
        print(num)
'''


# List comprehension
'''
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3x3

[[print(valor) for valor in lista] for lista in matriz]
'''


# Outros exemplos, gerando uma matriz identidade
'''
identidade = [[1 if coluna == linha else 0 for coluna in range(10)] for linha in range(10)]
[print(i) for i in identidade]
'''


# Gerando jogadas para o jogo da velha
'''
velha = [['X' if num % 2 == 0 else 'O' for num in range(3)] for linha in range(3)]
[print(i) for i in velha]
'''


# Gerando valores iniciais
'''
print([['*' for i in range(1, 4)] for j in range(1, 4)])
'''

