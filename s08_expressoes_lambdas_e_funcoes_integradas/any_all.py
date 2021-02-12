"""
Any e All

all() -> retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.
OBS: Um iterável vazio em bool é considerado falso, mas o all() retorna true

any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False.
"""

# Exemplo all()
'''
print(all([0, 1, 2, 3, 4]))  # Todos os números são verdadeiros? False
print(all([1, 2, 3, 4]))  # print(bool(4)) -> True
print(all([]))  # True
print(all((1, 2, 3, 4)))  # Pode ser uma tupla # True
print(all({1, 2, 3, 4}))  # Pode ser um set # True
print(all('0'))  # Pode ser uma string # True
'''
'''
nomes = ['Camila', 'Catarina', 'Caique', 'Cesar', 'Cristiano']
print(all(nome[0] == 'C' for nome in nomes))
'''

# Exemplo any()
'''
print(any([0, 0, 1]))  # True
print(any({False, False, False, True}))  # True
print(any((0, 0, 0, 44)))  # True
print(any((0, [], 0, 0)))  # False
print(any((0, 0, 0, None)))  # False
print(any((None,)))  # False
print(any(('0', False, 0)))  # False
print(any([]))  # False
'''
'''
nomes = ['Camila', 'Catarina', 'Caique', 'Cesar', 'Cristiano', 'Vanessa']
print(any(nome[0] == 'V' for nome in nomes))
'''