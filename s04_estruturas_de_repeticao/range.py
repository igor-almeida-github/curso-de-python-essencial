"""
Ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequências númericas não de forma aleatória,
mas sim de maneira especificada.

Formas gerais:

# Forma 1
range(valor de parada)
OBS: valor_de_parada não inclusive (inicio padrão 0, e passo de 1 em 1)

# Exemplo forma 1:
for numero in range(11):
    print(numero)

# Forma 2
range(valor_de_inicio, valor_de_parada)
OBS: valor_de_parada não inclusive (passo de 1 em 1)

# Exemplo forma 2
for num in range(5, 10):
    print(num)


# Forma 3
range(valor_de_inicio, valor_de_parada, passo)
OBS: valor_de_parada não inclusive, início, fim e passo especificados pelo usuário

# Exemplo forma 3
for num in range(15, 99, 6):
    print(num)


# Forma 4 (inversa)
range(valor_de_inicio, valor_de_parada, passo(negativo))
OBS: valor_de_parada não inclusive, início, fim e passo especificados pelo usuário

# Exemplo forma 4
for num in range(100, 10, -5):
    print(num)

# Bônus, criação de listas
lista = list(range(1, 10, 1))
"""


