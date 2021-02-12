"""
Generator Expression

Em aulas anteriores nos estudamos:
- List Comprehension;
- Dictionary;
- Set Comprehension;

Não vimos:
- Tuple comprehension ...porque elas se chamam Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassio', 'Critina', 'Vanessa']

"""
'''
nomes = ['Carlos', 'Camila', 'Carla', 'Cassio', 'Critina', 'Vanessa']
print(nome[0] == 'C' for nome in nomes)
print(type(nome[0] == 'C' for nome in nomes))
'''
'''
nomes = ['Carlos', 'Camila', 'Carla', 'Cassio', 'Critina', 'Vanessa']
# List Comprehension
print([nome[0] == 'C' for nome in nomes])

# Generator
print(nome[0] == 'C' for nome in nomes)
'''
'''
from sys import getsizeof
# Qual é a utilidade de getsizeof()? Retorna a quantidade de bytes em memória do elemento passado como parâmetro
print(getsizeof('Geek'))  # Strings ocupam (25 + número de caracteres) bytes da memória
print(getsizeof(2))
print(getsizeof(True))
'''
'''
from sys import getsizeof

# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x*10 for x in range(1000)])
print(f'List Comprehension: {list_comp} bytes')

# Gerando um set de números com Set Comprehension
set_comp = getsizeof({x*10 for x in range(1000)})
print(f'Set Comprehension: {set_comp} bytes')

# Gerando um dictionary de números com Dictionary Comprehension
dict_comp = getsizeof({x: x*10 for x in range(1000)})
print(f'Dictionary Comprehension: {dict_comp} bytes')

# Gerando uma lista de números com Generator
gen = getsizeof(x * 10 for x in range(1000))
print(f'Generator: {gen} bytes')
'''
'''
# Pode-se iterar nos Generators:
gen = (x for x in range(10) if x % 2 == 0)
for i in gen:
    print(i)
print(gen)
'''
