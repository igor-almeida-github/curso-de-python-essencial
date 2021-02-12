"""
Documentando funções com Docstrings

OBS: Podemos ter acesso a documentação de uma função em Python utilizando a propriedade especial __doc__

Podemos ainda fazer acesso a documentação com a função help
"""

# Exemplo 1
'''

def diz_oi():
    """ Uma função simples que retorna a string 'oi' """
    return 'oi'


print(diz_oi())
help(diz_oi)
print(diz_oi.__doc__)
'''


# Exemplo 2


def exponencial(num, pot=2):
    """
    Função que retorna por padão o quadrado de 'num' ou o 'num' elevado a potência 'pot' informada.
    :param num: Base
    :param pot: Expoente (Padrão 2)
    :return: Base elevado ao expoente
    """
    return num ** pot


print(exponencial(2, 4))
help(exponencial)
print(exponencial.__doc__)

