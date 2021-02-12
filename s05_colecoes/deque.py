"""
Módulo Collections - Deque
https://docs.python.org/3/library/collections.html#collections.deque
Podemos dizer que o Deque é  uma lista de alta performace.
"""

# Importa
from collections import deque
deq = deque('igor')
print(deq)

# Adicionando elementos no deque
deq.append('R')
deq.appendleft('L')
print(deq)

# Remover elementos
deq.pop()
deq.popleft()
print(deq)
