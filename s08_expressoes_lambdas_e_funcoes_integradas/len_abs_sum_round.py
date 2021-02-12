"""
Len, Abs, Sum, Round

len() -> Retorna o tamanho (ou seja, o número de itens) de um iterável.
abs() -> Retorna o valor absoluto (módulo) de um número inteiro ou real.
sum() -> Recebe como parâmetro um iterável, podendo receber um valor inicial, e retorna a soma total dos elementos,
incluindo o valor inicial. OBS: O valor inicial defaut = 0
round() -> Retorna um número arredondado para n digito de precisão após a casa decimal. Se a precisão não for informada
retorna o inteiro mais próximo da entrada.
"""

# Só para revisar - len
'''
print(len('Igor Almeida'))  # 12
print(len([1, 2, 3, 4]))  # 4
print(len((1, 2, 3, 4)))  # 4
print(len({1, 2, 3, 4}))  # 4
print(len({1: 0, 2: 0, 3: 0, 4: 0}))  # 4
print(len(range(0, 10)))  # 10

# Por debaixo dos panos, quando utilizamos a função len() o Python faz o seguinte:
print('Geek University'.__len__())  # Dunder len
'''
# Exemplos abs()
'''
print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))
'''
# Exemplos sum()
'''
print(sum([1, 2, 3, 4]))  # 10
print(sum([1, 2, 3, 4], -10))  # 20
print(sum([0.05, 0.05, -0.05]))  # 0.05
print(sum({'a': 1, 'b': 1, 'c': 1}.values()))  # 3
print(sum({1, 2, 3}))  # 6
'''
# Exemplos round()
'''
print(round(10.2))  # 10
print(round(10.5))  # 11 (se estiver no meio, arredonda para baixo)
print(round(10.6))  # 11
print(round(-8.8963322485, 4))  # -8.8963
'''

