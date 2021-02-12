"""
Decorators com diferentes assinaturas

Em Python, a assinatura de uma função é representada pelo seu nome e parâmetros de entrada.
"""


# Padrão de projeto chamado Decorator Pattern (resolve o problema de número desconhecido de argumentos)
'''
def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'


@gritar
def lol():
    return 'lol'


print(saudacao('igor'))
print(ordenar('picanha', 'cheddar'))
print(lol())
'''


# Decorator com argumentos
'''
def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if not args or args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('Pizza')
def comida_favorita(*args):
    return args


print(comida_favorita('Pizza', 'Hamburguer'))


@verifica_primeiro_argumento(10)
def soma(*args):
    return sum(args)


print(soma(11, 20))
'''

