"""
Funções com Parâmetro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:
- Entrada -> Processamento -> Saída

Se a gente pensar em funções, já sabemos que temos funções que:
- Não possuem entrada, mas possuem saída;
- Não possuem saída, mas possuem entrada;
- Possuem entrada e saída;
- Não possuem nem entrada e nem saída;

"""


# Exemplo 1
'''
def quadrado(num):
    # return num * num  # Vezes
    return num ** 2  # ** significa elevado


print(quadrado(5))
# print(quadrado())  # TypeError, o argumento está faltando
'''


# Exemplo 2
'''
def cantar_parabens(nome):
    print('Parabéns para você')
    print('nessa data querida')
    print('muitas felicidades')
    print('muitos anos de vida')
    print(f'viva {nome}')


cantar_parabens('Igor')
'''


# Funções podem ter n parâmetros de entrada. Ou seja podemos receber como entrada em uma função, quantos
# parâmetros forem necessários. Eles são separados por vírgulas.

# Exemplo de múltiplas entradas:
'''
def soma(a, b, msg):
    print(msg)
    return a + b


print(soma(4, 5, 'Igor'))

# OBS: Se a gente informar um número errado de parâmetros ou argumentos, teremos TypeError
'''


# Nomeando parâmetros
'''
def nome_completo(nome, sobrenome):  # evitar nomes genéricos nos parâmetros como def nome_completo(string1, string2)
    return f'Seu nome completo é {nome} {sobrenome}'


print(nome_completo('igor', 'almeida'))
# OBS: A ordem dos parâmetros importa
'''


# Diferença entre parâmetros e argumentos:
# Parâmetros são variáveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função;


# Argumentos nomeados (Keyword Arguments)
# Caso utilizemos nomes dos parâmetros nos argumentos para informa-los, podemos utilizar qualquer ordem
'''

def nome_completo(nome, sobrenome, idade):
    return f'Seu nome completo é {nome} {sobrenome} e sua idade é {idade}'


print(nome_completo(sobrenome='almeida', idade='23', nome='igor'))
'''


# Desempacotando
def soma(a, b, c):
    print(a + b + c)


# Isso foi inserido para testar o dunder no arquivo dunder
print(__name__)  # funcoes_com_parametro
if __name__ == '__main__':
    lista = [1, 2, 3]
    tupla = (1, 2, 3)
    conjunto = {1, 2, 3}
    soma(*lista)
    soma(*tupla)
    soma(*conjunto)

    dicionario = dict(a=1, b=2, c=3)
    soma(**dicionario)


# OBS: os nomes das chaves em um dicionário devem ser os mesmos dos parâmetros da função
