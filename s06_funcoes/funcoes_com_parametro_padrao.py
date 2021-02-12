"""
Funções com Parâmetro Padão (Default Parameters)
- Funções onde a passagem de parâmetros é opcional

"""

# Exemplo de função com passagem de parâmetro opcional
'''
print('igor', 2)
print(1, 2, 3)
print()
'''


# Exemplo de função onde a passagem de parâmetro é obrigatória
'''
def quadrado(numero):
    return numero ** 2


print(quadrado(4))
'''


# Criando função com a passagem de parâmetro opcional
'''
def exponencial(num, exp=2):  # Se exp não for informado, por padrão, deseja-se elevar ao quadrado
    return num ** exp


print(exponencial(10, 4))
print(exponencial(10))
print(exponencial(2))

# OBS: Se usuário passar somente 1 parâmetro, este será atribuido ao parâmetro numero, e será calculado o quadrado
# deste número, pois por padrão a potência é 2.
'''


# Em funções Python, os parâmetros com valores default DEVEM sempre estar o final da declaração.
'''
# ERRO!
def teste(nome='igor', idade):  # ERRO: non-default argument follows default argument
    return f'{nome} tem {idade} anos'


print(teste('julio', 22))
'''


# Outros exemplos:
'''
def soma(num1, num2):
    return num1 + num2


print(soma(4, 3))
'''


# Exemplo mais complexo
'''
def mostra_info(nome='Igor', idade=23):
    if nome == 'Igor' and idade == 23:
        return 'Olá Adm'
    elif nome == 'Igor':
        return 'Você está mentindo, eu sei que você não é o Igor'
    return f'Olá {nome} você está com {idade} anos'


print(mostra_info('João', 55))
print(mostra_info(idade=55))
print(mostra_info())
print(mostra_info('Jorge'))
'''


# Por que trabalhar com parâmetros com valor default
'''
- Nos permite ser mais flexíveis nas funções;
- Evita erros com parâmetros incorretos
- Nos permite trabalhar com exemplos mais legiveis de código
'''


# Quais tipos de dados podemos utilizar como valores default para parâmetros?
'''
- Qualquer tipo de dado: Números, strings, floats, boleanos, lista, tuplas, dicionários, funções e etc;
'''


# Exemplos (passando funções como parâmetros)
'''
def soma(num1, num2):
    return num1 + num2


def subtracao(num1, num2):
    return num1 - num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


print(mat(4, 4))
print(mat(10, 5, subtracao))
'''


# Escopo - Para evitar problemas e confusões ...
'''
# Variáveis globais
# Variáveis locais

nome = 'igor'  # Variável global


def diz_oi():
    sentimento = 'legal'
    nome = 'Batman'  # Variável local
    return f'Oi {nome} que {sentimento}'


print(diz_oi())
print(nome)
# print(sentimento)  # NameError pois a variável sentimento é de escopo local e só existe dento de diz_oi()


# OBS: Se tivermos uma variável local com o mesmo nome de uma global, a local terá preferência
'''


# Atenção com variáveis globais (Se puder evite)
'''
total = 0


def incrementa():
    total = total + 1  # UnboundLocalError, essa variável ainda não foi inicializada dentro da função incrementa
    return total


print(incrementa())
'''


# Com o erro acima corrigido:
'''
total = 2


def incrementa():
    global total  # Inicializa a variável global 'total' dentro da função incrementa, permitindo seu uso
    total = total + 1
    return total


print(incrementa())
print(incrementa())
print(incrementa())
'''


# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável

def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()


print(fora())
# print(dentro())  # ERRO: O escopo da função 'dentro()' é somente dentro da função 'fora()'






