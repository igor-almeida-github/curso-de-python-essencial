"""
Trabalhando com Módulos Builtin (módulos integrados, que já vem instalados no Python)

https://docs.python.org/3/py-modindex.html
________________________
|Python|Módulos builtin|
________________________
"""
# Importando módulo inteiro
'''
import random

print(random.random())
'''
# Utilizando alias (apelidos) para módulos
'''
import random as rd

print(rd.random())
'''
# Utilizando alias (apelidos) para funções
'''
from random import random as rd

print(rd())
'''
# Podemos importar todas as funções de um módulo utilizando o *
'''
from random import *

print(random())
'''
# Importando multiplas funções de um mesmo módulo
'''
from random import random, randint, shuffle

print(random())
print(randint(1, 10))
lista = [1, 2, 3]
shuffle(lista)
print(lista)
'''
# Utilizando alias (apelidos) para multiplas funções
'''
from random import random as rd, randint as rdi

print(rd())
print(rdi(1, 10))
'''
# Costumamos utilizar tuple para colocar mútiplos imports de um mesmo módulo
'''
from random import (
    random,
    randint,
    shuffle
)

print(random())
print(randint(1, 10))
lista = [1, 2, 3]
shuffle(lista)
print(lista)
'''






