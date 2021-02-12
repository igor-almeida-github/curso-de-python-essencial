"""
Teste de Memória com Generators

Sequência de Fibonacci
1, 1, 2, 3, 5, 8, 13 ...
"""

'''
def fib_list(maximo):
    seq = [1, 1]
    while len(seq) < maximo:
        seq.append(seq[-1] + seq[-2])
    return seq


fib_list(100000)  # Usa muita memória
'''


# Usando geradores
'''
def fib_list(maximo):
    p = 0
    seq_2_ultimos = [0, 1]
    while p < maximo:
        yield seq_2_ultimos[1]
        p = p + 1
        seq_2_ultimos.append(seq_2_ultimos[0] + seq_2_ultimos[1])
        seq_2_ultimos.pop(0)


ger = fib_list(100000)  # Usa pouca memória

while True:
    try:
        next(ger)
    except StopIteration:
        break
'''

