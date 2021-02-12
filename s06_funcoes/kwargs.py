"""
**kwargs

Poderia chamar este parâmetro de **xis, mas por convenção chamamos de **kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca valores extras
em uma tupla, o **kwargs exige que utilizemos parâmetros nomeados, e transforma
esses parâmetros extras em um dicionário.
"""


# Exemplo 1
'''
def cores_favoritas(**kwargs):
    for nome, cor in kwargs.items():
        print(f'O(A) {nome.title()} gosta da cor {cor}')


cores_favoritas(igor='vermelho', joão='preto', angelina='roxo')
cores_favoritas()

# OBS: Os parâmetros *args e **kwargs não são obrigatórios
'''


# Exemplo 2
'''

def cumprimento_especial(**kwargs):
    if 'igor' in kwargs and kwargs['igor'] is 'Python':  # Aqui ele testa a primeira sentença, se falsa, nem testa a 2.
        return 'Você recebeu uma saldação Pythônica'
    return 'O que?'


print(cumprimento_especial(igor='Python', carro='Playstation', gorila='Nada a ver'))
print(cumprimento_especial())
print(cumprimento_especial(igor='Psdfsdfythsdon'))
print(cumprimento_especial(igsadasdr='Python'))
'''


# Nas nossas funções, podemos ter (NESTA ORDEM):
'''
- Parâmetros obrigatórios;
- *args;
- Parâmetros default (não obrigatórios);
- **kwargs;
'''


# Usando todos os parâmetros simultaneamente: (A ORDEM ACIMA DEVE SER RESPEITADA)


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    estado_civil = {False: 'casado', True: 'solteiro'}
    print(f'{nome} tem {idade} anos e é {estado_civil[solteiro]}')
    print(args)
    print(kwargs)


minha_funcao(22, 'igor', 1, 2, 3, 4, 5, 6, 7, solteiro=True, feliz='sim', python='legal')
print(60*'-')
minha_funcao(22, 'igor')
print(60*'-')
minha_funcao(22, 'igor', agua='bebida', pizza='comida')


# Entenda por quê é importante manter a ordem dos parâmetros na delcaração
'''
# Função com a ordem correta de parâmetros:
def mostra_info(a, b, *args, nome='Igor', **kwargs):
    return [a, b, args, nome, kwargs]


# Função com a ordem incorreta:
def mostra_info2(a, b, nome='Igor', *args, **kwargs):
    return [a, b, args, nome, kwargs]


print(mostra_info(10, 20, 1, 2, 3, 4, nome='Jhon', helicoptero='voa'))
# print(mostra_info2(10, 20, nome='Jhon', 1, 2, helicoptero='voa'))  #SyntaxError
'''


# Desempacotar com **kwargs
'''

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


dicionario = {'nome': 'angelina', 'sobrenome': 'jolie'}

print(mostra_nomes(**dicionario))
'''




