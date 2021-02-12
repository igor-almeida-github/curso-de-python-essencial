"""
Módulo Collections: Ordered Dict
https://docs.python.org/3/library/collections.html#collections.OrderedDict
"""

# Em um dicionário a ordem de inseerção dos elementos não garantida.
'''
dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(dic)

for chave, valor in dic.items():
    print(f'chave = {chave} e valor = {valor}')
'''

# Fazendo import (OrderedDict é um dicionário que garante a ordem de inserção dos elementos)
'''
from collections import OrderedDict
dic = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
print(dic)

for chave, valor in dic.items():
    print(f'chave = {chave} e valor = {valor}')
'''

# Entendendo a diferença entre dict e OrderedDict
from collections import OrderedDict

# Dicionários comuns
dic_c1 = {'a': 1, 'b': 2}
dic_c2 = {'b': 2, 'a': 1}
print(dic_c1 == dic_c2)  # True, já que a ordem não importa para o dicionário

# Dicionários OrderedDict
dic_oc1 = OrderedDict({'a': 1, 'b': 2})
dic_oc2 = OrderedDict({'b': 2, 'a': 1})
print(dic_oc1 == dic_oc2)  # False, já que a ordem de inserção é preservada no OrderedDict
