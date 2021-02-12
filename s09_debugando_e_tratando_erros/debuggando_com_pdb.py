"""
Debuggando com PDB
PDB - Python Debugger
Bug -> Inseto
"""


# OBS: A utilização do print para debugar código é uma prática ruim:
'''
def dividir(a, b):
    print(f'a:{a}  b:{b}')
    try:
        return int(a) / int(b)
    except (TypeError, ZeroDivisionError, ValueError) as err:
        return f'Ocorreu um erro: {err}'


print(dividir(4, 7))
'''
# Existem formas mais profissionais de se fazer esse debug, utilizando o debbuger.
# Em Python, podemos fazer isso em diferentes IDEs, como o Pycharm ou utilizando o PDB - Python Debugger
'''

# Exemplo com o Pycharm
def dividir(a, b):
    try:
        return int(a) / int(b)
    except (TypeError, ZeroDivisionError, ValueError) as err:
        return f'Ocorreu um erro: {err}'


print(dividir(4, 0))
'''
# Exemplo com o PDB - Python Debugger - Exemplo 1
# Para utilizar o Python Debugger, precisamos* importar a biblioteca pdb e então utilizar a função set_trace()
# Comandos básicos do PDB
# l (lista onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)
'''
import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)
'''
# Exemplo com o PDB - Python Debugger - Exemplo 2
# Para utilizar o Python Debugger, precisamos* importar a biblioteca pdb e então utilizar a função set_trace()
# Comandos básicos do PDB
# l (lista onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)
'''
nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Por quê utilizar este formato?
# O debug é utilizado durante o desenvolvimento. Costumamos realizar todos os imports de bibliotecas no início
# do arquivo. Ao invés de colocarmos o import do pdb no início do arquivo, nós colocamos somente
# onde vamos debuggar, e ao finalizar já fazemos a remoção, pois é mais rápido.
'''
# Exemplo com o PDB - Python Debugger - Exemplo 3
# Para utilizar o Python Debugger, precisamos* importar a biblioteca pdb e então utilizar a função set_trace()
# * A partir Python 3.7 não é mais necessário importar a biblioteca pdb, pois o comando de debug foi incorporado
# como função built-in (integrada) chamada breakpoint()
# Comandos básicos do PDB
# l (lista onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)
'''
nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)
'''
# OBS: Cuidado com conflitos entre nomes de variáveis e os comando do pdb
# Como os nomes das variáveis são os mesmo dos comandos do pdb, devemos utilizar o comando p para imprimir
# as variáveis. Ou seja: p nome_da_variavel
# Além disso, nada de colocar nomes não representativos em variáveis. Sempre optar por nomes significativos.
'''
def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c


print(soma(1, 2, 3, 4))
'''
