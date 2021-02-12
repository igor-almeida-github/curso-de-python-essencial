"""
Try / Except / Else / Finally

Dicas de quando e onde tratar código:
TODA ENTRADA DEVE SER TRATADA!
OBS: A função do usuário é DESTRUIR seu sistema.

Else -> É executado somente se não ocorrer o erro.

"""
# Problema:
'''
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Entrada inválida')
print(f'Você digitou {num}')  # Se a entrada for inválida, isso é executado obtendo NameError, num não definido.
'''
# Exemplo solução: (else)
'''
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Entrada inválida')
else:
    print(f'Você digitou {num}')
'''
# Finally - O bloco finally é SEMPRE executado. Indenpendente se houve exceção ou não, ou seja, mesma coisa de
# escrever comando no final.
'''
try:
    num = int(input('Informe um número: '))  # Tenta executar
except ValueError:
    print('Você não digitou um valor válido.')  # Executa somente se ocorrer erro
else:
    print(f'Você digitou {num}')  # Executa somente se não ocorrer erro
finally:
    print('Executando o finally')  # Executa de qualquer jeito
# OBS: o finally geralmente é utilizado para fechar ou desalocar recursos.
'''
# Exemplo mais complexo ERRADO - Deve-se preferêncialmente tratar as entradas dentro das funções.
'''
def dividir(a, b):
    return a / b


try:
    num1 = int(input('Informe o primeiro número: '))
except ValueError:
    print('O valor precisa ser numérico')
else:
    try:
        num2 = int(input('Informe o segundo número: '))
    except ValueError:
        print('O valor precisa ser numérico')
    else:
        print(dividir(num1, num2))
'''
# Exemplo mais complexo CORRETO - Você é responsável pelas entradas das suas funções. Então, trate-as!
'''
def dividir(a, b):
    try:
        return int(a) / int(b)
    except TypeError:
        return 'Tipo incorreto'
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Divisão por 0 impossível'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))
'''
# Exemplo semi-genérico
'''
def dividir(a, b):
    try:
        return int(a) / int(b)
    except (TypeError, ZeroDivisionError, ValueError) as err:
        return f'Ocorreu um erro: {err}'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))
'''



