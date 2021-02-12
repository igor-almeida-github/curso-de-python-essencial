"""
Loop for - Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis
Exemplos de iteráveis:
- String
    nome = 'igor'
- Lista
    lista = [1, 2, 3, 7, -12]
- Range
    numeros = range(min, max, inc)

for i in range(10):  # Printa os número de 0 a 9 de 1 em 1
    print(i)
#  ------------------------------------------------------------------------------
for i in range(50, 100, 10):  # Printa os números de 50 até 90 indo de 10 em 10
    print(i)
#  ------------------------------------------------------------------------------
t = [10, 20, 30, 40]
for i in t:
    print(i)
#  ------------------------------------------------------------------------------
t = 'ola mundo'
for i in t:
    print(i)
#  ------------------------------------------------------------------------------
for i in [10, -3, 4.4, 12]:
    print(i)
#  ------------------------------------------------------------------------------
# Números primos:

maximo = 1

while True:

    total_de_numeros = 0

    for i in range(2, maximo+1):
        primo = True
        for j in range(2, i):
            if i % j is 0:
                primo = False
        if primo is True:
            total_de_numeros += 1
    print(f'{maximo} {total_de_numeros}')

    maximo += 1

Enumerate:
(0, i), (1, g), (2, o), ...

nome = 'igor almeida'

for i, v in enumerate(nome):
    if v == 'i':
        print(i)
        
# O underline descarta o valor do indice, para 
não armazena-lo em nenhuma variável, caso ele não seja necessário
for _, v in enumerate(nome):  
        print(v)
# ----------------------------------------------------------------------------
nome = 'igor almeida'

for i in enumerate(nome):
    print(i)

#  ----------------------------------------------------------------------------
nome = 'igor almeida'

for i in nome:
    print(i, end='')  # Imprime sem saltar linha

# --------------------------------------------------------------
# Concatenação de strings

nome = 'igor'
nome += ' almeida'
print(nome)
nome = nome * 3  # O nome repetido 3 vezes é armazenado em nome
print(nome)

#  -------------------------------------------------------------
# print de unicodes
# U+1F630 é um unicode
# Substituir + por 000
# U0001F630

emoji = '\U0001F630'

for _ in range(3):
    for i in range(1, 5):
        print(emoji*i)

"""





