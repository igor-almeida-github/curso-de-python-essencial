"""
Decoradores (Decorators)

O que são decorators?

- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;
- O 'decorar' tem sentido de aprimorar, enfeitar e não de memorizar;
- Decorators também são exemplos de Higher Order Function;
- Decorators tem uma sintaxe própria, usando "@" (Syntact Sugar)



"""


# Decorators como funções (Sintaxe não recomendada / Sem Açucar Sintático)
'''
def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia')
    return sendo


def saudacao():
    print('Seja bem-vindo(a)')


teste = saudacao
teste()
print('--------------------------')
teste = seja_educado(saudacao)
teste()
'''


# Decorators com Syntax Sugar
'''
def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia')
    return sendo


@seja_educado
def saudacao():
    print('Seja bem-vindo(a)')


saudacao()
'''

'''
def adc_nome(fun):  # Decorator Function
    def funcao_modificada(num):
        print('igor')
        fun(num)
    return funcao_modificada


@adc_nome  # Decorator
def mostra_num(num):
    print(num)


mostra_num(2)
'''

# OBS: Não confunda Decorator com Decorator Function

