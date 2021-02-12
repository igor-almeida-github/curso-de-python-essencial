"""
Entendendo o *args

- O *args é um parâmetro, como outro qualquer. Isso significa que você poderá chamar de qualquer coisa, desde que começe
com  asterisco.

Exemplo:
*xis
Mas por convenção, utilizamos o *args para definí-lo
Mas o que é o *args?
O parâmetro *args utilizado em um função, coloca os valores extras informados como
entrada em uma tupla. Então desde já, lembre-se que tuplas são imutáveis.
"""

# Exemplo antigo:
'''

def soma(num1, num2, num3):
    return num1 + num2 + num3


print(soma(2, 3, 4))
# print(soma(2, 3))  # TypeError
# print(soma(2, 3, 4, 4))  # TypeError
'''


# Forma nova de realizar a mesma coisa, mas sem o TypeError (*args):
'''

def soma(nome, qualidade, *args):

    return f'Olá {nome} você é muito {qualidade} e sua soma deu {sum(args)}'


print(soma('joao', 'inteligente', 2, 3, 4))
print(soma('lucas', 'legal', 2, 3))
print(soma('juca', 'esperto', 2, 3, 4, 4))
print(soma('carlos', 'sabio', 1, 1, 1, -1, 1.2))
'''


# Outro exemplo de uso do *args
'''

def verifica_info(*args):
    if 'Igor' in args and 'Almeida' in args:
        return 'Bem vindo, você está autorizado'
    return 'Invasor detectado'


print(verifica_info('Igor', 'Almeida'))
print(verifica_info('Almeida', 'Igor', None, True))
print(verifica_info('Igor Almeida'))
print(verifica_info('Playstation', '2', 'Video game'))
'''


# O que acontece se passarmos uma lista como argumento? veja:
'''

def soma(*args):
    print(args)  # ([2, 3, 4],)
    return sum(args)


# print(soma([2, 3, 4]))  # TypeError
'''

# Agora a maneira correta de passar uma lista como argumento (Desempacotador):
'''

def soma(*args):
    print(args)
    return sum(args)


print(*[2, 3, 4])
print(soma(*[2, 3, 4]))  # Colocando asterisco cada valor dentro da lista é passado como um argumento diferente


# OBS: O asterisco serve para que informemos ao Python que estamos passando como argumento uma coleção de dados, desta
# forma, ele saberá que precisará antes desempacotar estes dados.
'''










