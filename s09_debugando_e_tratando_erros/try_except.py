"""
O bloco try/except

Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso código. Previnindo assim que o programa
pare de funcionar e o usuário receba mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    //execução problemática
except:
    //O que deve ser feito em caso de problema
"""

# Exemplo 1 - Tratando um erro genérico (não recomendado PEP 8)
'''
try:
    geek()
except:
    print('Deu problema')
'''
# Exemplo 2
'''
try:
    len(5)
except:
    print('Deu problema')
'''
# OBS: Tratar erro de forma genérica não é a melhor forma de tratamento de erros. O ideal é SEMPRE tratar de
# forma específica.
# Exemplo 3 - Tratando um erro específico
'''
try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente')  # NameError - executa isso.
'''
'''
try:
    len(5)
except NameError:
    print('Você está utilizando uma função inexistente')  # TypeError - não executa isso.
'''
# Exemplo 4
'''
try:
    len(5)
except TypeError:
    print('Você está passando um argumento do tipo errado')  # TypeError - não executa isso.
'''
# Exemplo 5 - Tratando um erro específico com detalhes do erro.
'''
try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')
'''
# Exemplo 6 - Podemos efetuar diversos tratamentos de erros de uma só vez.
'''
try:
    # len(5)
    geek()
except NameError as err:
    print(f'Deu NameError: {err}')
except TypeError as err:
    print(f'Deu TypeError: {err}')
'''
# Exemplo 7
'''
def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError as err:
        return f'chave não encontrada: {err}'
    except TypeError as err:
        return f'Erro: {err}'


dic = {'nome': 'Geek'}

print(pega_valor(dic, 1))
'''


