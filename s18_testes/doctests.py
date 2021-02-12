"""
Doctests - São testes que colocamos na docstring das funções/métodos Python.

Para rodar um test do doctest:

python -m doctest -v nome_do_modulo.py


"""

'''
def soma(a, b):
    """Soma os números a e b

    >>> soma(1, 2)
    3

    >>> soma(4, 6)
    10

    """
    return a + b


print(soma(3, 4))
'''


# Outro Exemplo, aplicando o TDD
'''
def dobrar_valores(valores):
    """
    Duplica os valores em um lista

    >>> dobrar_valores([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> dobrar_valores([])
    []

    >>> dobrar_valores(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']

    >>> dobrar_valores([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * elemento for elemento in valores]
'''


# Erro inesperado...
'''
def fala_oi():
    """Fala oi

    >>> fala_oi()
    'oi'
    """
    return "oi"
# OBS: Dentro do doctest, o Python não reconhece string com aspas duplas. Precisa ser aspas simples.
'''


# Um último caso estranho... Passa no Pycharm, mesmo com espaço após o True

def verdade():
    """Retorna verdade
    >>> verdade()
    True
    """
    return True









