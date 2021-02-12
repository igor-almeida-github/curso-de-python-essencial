"""
Reduce

OSB: A partir do Python3+ a função reduce() não é mais uma função integrada (built-in). Agora temos que importar
e utilizar esta função a partir do módulo 'functools'

Guido Van Rossum: Utilize a função reduce() se você realmete precisa dela. Em todo caso,
99% das vezes um loop for é mais legível.

Para entender o reduce()

# Imagine que você tem uma coleção de dados:

dados = [a1, a2, a3, ..., an]

# E você tem uma função que recebe dois parâmetros:

def funcao(x, y):
    return x * y

# Assim como map() e filter() a função reduce() recebe dois parâmetros: a função e o iterável.
# reduce(funcao, dados)

A função reduce() funciona da seguinte forma:
   Passo 1: res1 = f(a1, a2)  # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado.
   Passo 2: res2 = f(res1, a3) # Aplica a função passando o resultado do passo1 mais o terceiro elemento e guarda o res.
   Isso é repetido até o final

Alternativamente podemos ver reduce como:
... funcao(funcao(funcao(funcao(a1, a2), a3), a4), a5) ... an)

Para usar o reduce precisamos de uma função que recebe 2 parâmetros, tem que ser 2 exatamente

"""

import functools
dados = [2, 3, 2, 2, 2]


def produto(x, y):
    return x * y


print(functools.reduce(produto, dados))
print(functools.reduce(lambda x, y: x * y, dados))  # lambda também serve

# Utilizando um for

res = produto(dados[0], dados[1])
for i in range(2, len(dados)):
    res = produto(res, dados[i])
print(res)

