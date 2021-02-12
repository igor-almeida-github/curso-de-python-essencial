"""
Lambdas

Conhecidas por Expressões lambdas, ou simplesmente lambdas são funções sem nome, ou seja,
funções anônimas.

"""


# Expressão Lambda
'''
lambda x: 3 * x + 1
'''


# Como utilizar? (Uma forma póssivel, mas não é legal, não segue PEP8)
'''
calc = lambda x: 3 * x + 1
print(calc(4))
'''


# Podemos ter expressões lambdas com múltiplas entradas
'''
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo('    anGelina', '  JoliE    '))
'''


# Em lambdas podemos ter nenhuma ou várias entradas
'''
amar = lambda: 'Como não amar Python?'
uma = lambda x: 3 * x + 1
duas = lambda x, y: (x * y) ** 0.5
tres = lambda x, y, z: x + y + z

print(amar())
print(uma(6))
print(duas(1, 2))
print(tres(1, 2, 3))

# OBS: Se passarmos mais argumentos do que parâmetros teremos TypeError
'''


# Outro exemplo (FORMA CORRETA DO USO DE LAMBDAS: PASSANDO DIRETO DENTRO DE ONDE ELA SERÁ USADA)
'''
nomes = ['Igor Goulart de Almeida', 'R. B. Nunes', 'Arthut C. Rocha', 'Anne Frank', 'Douglas Adams']
print(nomes)
nomes.sort(key=lambda nome: nome.split(' ')[-1].lower())  # Ordena pelo sobrenome
print(nomes)
'''


# Função quadratica
'''
def gerador_f_quad(a, b, c):
    """ Retorna a função quadratica f(x) = a * x ** 2 + b * x + c """
    return lambda x: a * x ** 2 + b * x + c


teste = gerador_f_quad(2, 3, -5)
print(teste(2))
print(gerador_f_quad(2, 3, -5)(2))
'''



