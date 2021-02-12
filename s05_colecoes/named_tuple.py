"""
Módulo Collections - Named Tuple
https://docs.python.org/3/library/collections.html#collections.namedtuple
# Recap
tupla = (1, 2, 3)
print(tupla[1])

Named Tuple -> São tuplas diferenciadas, onde, especificamos um nome para a mesma e tamém parâmetros.

"""

# Importando
from collections import namedtuple

# Precismos definir o nome e parâmetros

# Forma 1 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')

# Acessando dados
print(ray)
print(ray[0])
print(ray.idade)

print(ray.index('Ray'))
print(ray.count(2))
