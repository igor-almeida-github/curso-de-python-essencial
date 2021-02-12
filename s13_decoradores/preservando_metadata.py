"""
Preservando metadatas com wraps
Metadados -> São dados intrínsecos em arquivos.
Wraps -> São funções que envolvem elementos com diversas finalidades.
"""
from functools import wraps

# Problema
'''
def ver_log(funcao):
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) de outra"""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois números."""
    return a + b


print(soma(1, 1))
print('________________________')
print(soma.__name__)
print(soma.__doc__)
'''


# Resolução do Problema
'''
def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) de outra"""
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois números."""
    return a + b


print(soma(1, 1))
print('________________________')
print(soma.__name__)
print(soma.__doc__)
'''

