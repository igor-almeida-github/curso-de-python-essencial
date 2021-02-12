"""
Teste de Velocidade com Expressões Geradoras


"""
import time

'''
# Generators (Geradores)

def nums():
    for num in range(1, 10):
        yield num


ge1 = nums()

print(ge1)  # Generator

print(next(ge1))  # 1
print(next(ge1))  # 2
print(next(ge1))  # 3 ...

# Generator Expression

ge2 = (num for num in range(1, 10))
print(ge2)
print(next(ge2))  # 1
print(next(ge2))  # 2
print(next(ge2))  # 3 ...
'''
# Realizando o teste de velocidade
'''
# Generator expression
inicio = time.time()
sum(num for num in range(10_000_000))
fim = time.time()
print(fim - inicio)

# List comprehension
inicio = time.time()
sum([num for num in range(10_000_000)])
fim = time.time()
print(fim - inicio)
'''
