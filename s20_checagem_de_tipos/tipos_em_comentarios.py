import math


# Errado, duplicado
'''
def circunferencia(raio: float) -> float:
    # type: (float) -> float
    return 2 * math.pi * raio
'''

'''
def circunferencia(raio):
    # type: (float) -> float
    return 2 * math.pi * raio


print(circunferencia(8))
# print(circunferencia('igor'))
'''


def cabecalho1(texto, alinhamento=True):
    # type: (str, bool) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'


cabecalho1(43, 'igor')


def cabecalho2(
        texto,  # type: str
        alinhamento=True  # type: bool
):  # type: (...) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'


cabecalho2(43, 'igor')

nome = 'Igor'  # type: str
