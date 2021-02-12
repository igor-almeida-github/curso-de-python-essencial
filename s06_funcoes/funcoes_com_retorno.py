"""
Funções com retorno

OBS: Sobre a palavra reservada return
- Ela finaliza a função, ou seja, ela sai da execução da função;
- Podemos ter em uma função, diferentes returns;
- Podemos em um função, retornar qualquer tipo de dado e até mesmo multiplos valores;
"""


# Funções com retorno vs sem retorno:
'''
numeros = [1, 2, 3]

ret_pop = numeros.pop()
print(f'Retorno de pop: {ret_pop}')
ret_pr = print(numeros)
print(f'Retorno de print: {ret_pr}')
'''


# Exemplo de função sem retorno
'''

def quadrado_de_7():
    print(7*7)


ret = quadrado_de_7()
print(f'Retorno: {ret}')
# OBS: Em Python, quando uma função não retorna nenhum valor, o retorno é none
'''


# Exemplo de função com retorno
'''
def quadrado_de_7():
    return 7 * 7


ret = quadrado_de_7()
print(f'Retorno: {ret}')
# Alternativamente
print(f'Retorno: {quadrado_de_7()}')
# OBS: Funções Python que retornam valores, devem retornar estes valores com a palavra reservada return
# OBS: Não precisamos necessariamente criar uma variável para receber o retorno de um função, podemos passar a
# execução da função para outras funções.
'''


# Refatorando a primeira função
'''
def diz_oi():
    return 'oi '


alguem = 'Igor'
print(diz_oi() + alguem)
'''


# Exemplo 1 - Demonstração da afirmação 'o return sai da função'
'''
def diz_oi():
    print('estou sendo executado antes o return')  # Será executada
    return 'oi'
    print('estou sendo executado após o return')  #  Não será executada


print(diz_oi())
'''


# Exemplo 2 - Demonstração da afirmação 'podemos ter diferentes returns'
'''
def nova_function():
    variavel = False
    if variavel:
        return -4
    elif variavel is None:
        return ['i']
    return 22.2


print(nova_function())
'''


# Exemplo 3 - Demo de 'Podemos em um função, retornar qualquer tipo de dado e até mesmo multiplos valores'
'''
def outra_func():
    return 2, 3, 4, 5


num1, num2, num3, num4 = outra_func()
print(num1, num2, num3, num4)
print(outra_func())
'''


# Vamos criar uma função para jogar a moeda
'''
from random import randint


def moeda():
    if randint(1, 2) is 1:
        return 'Cara'
    return 'Coroa'


print(moeda())
'''


# Erros comuns na utilização do retorno, que na verdade nem é erro, mas sim codificação desnecessária
'''
def e_impar():
    num = 5
    if num % 2 != 0:
        return True
    else:  # Desnecessário
        return False


print(e_impar())
'''





