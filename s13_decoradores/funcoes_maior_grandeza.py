"""
Funções de Maior Grandeza - Higher Order Functions - HOF

O que isso significa?
- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções que retornam outras funções
como resultado ou mesmo que podemos passar funções como argumentos para outras funções, e até mesmo criar variáveis
do tipo de funções nos nossos programas.

OBS: Na seção de funções, nós utilizamos isso.

Em Python, as funções são Cidadãos de Primeira Classe, First Class Citizen
"""

from random import choice

'''
# Exemplo - Definindo as funções
def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


print(calcular(3, 3, somar))
print(calcular(3, 3, diminuir))
print(calcular(3, 3, multiplicar))
print(calcular(3, 3, dividir))
'''

# Nested Function - Funções Aninhadas
# Em Python podemos também ter funções dentro de funções, que são conhecidas por Nested Functions
# ou também Inner Functions (Funções Internas).
'''

# Exemplo
def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui, ', 'Gosto muito de você, '))
    return humor() + pessoa


print(cumprimento('Igor'))
'''
# Retornando funções de outras funções
'''

def faz_me_rir():
    def rir():
        return choice(('hahahaha', 'lol', 'kkkkkkkkkk'))
    return rir


print(faz_me_rir())  # <function faz_me_rir.<locals>.rir at 0x03BD7B70>
print(faz_me_rir()())  # hahahaha' / 'lol' /'kkkkkkkkkk'
'''


# Inner Functions (Funções Internas / Nested Functions) podem acessar o escopo de funções mais externas
def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahahaha', 'lol', 'kkkkkkkkkk'))
        return f'{risada} {pessoa}'
    return dando_risada


print(faz_me_rir_novamente('Igor')())

