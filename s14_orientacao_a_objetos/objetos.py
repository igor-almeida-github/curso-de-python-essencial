"""
POO - Objetos

Objetos -> Instâncias da classe, ou seja, após o mapeamento do objeto do mundo real para sua representação
computacional, devemos poder criar quantos objetos forem necessários. Podemos pensar nos objetos/intâncias de uma
classe como variáveis do tipo definido na classe.
"""


class Lampada:

    def __init__(self, cor, tensao, luminosidade):
        self.__cor = cor
        self.__tensao = tensao
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O cliente {self.nome} diz oi')


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        ContaCorrente.contador = self.__numero
        self.__limite = limite
        self.__saldo = saldo
        self.cliente = cliente

    def mostra_cliente(self):
        print(f'O cliente é {self.cliente.nome}')


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


# Instâncias/Objetos
'''
lamp1 = Lampada('Amarela', 127, 1000)
print(f'A lampada está ligada? {lamp1.checa_lampada()}')
lamp1.ligar_desligar()
print(f'A lampada está ligada? {lamp1.checa_lampada()}')
cc1 = ContaCorrente(5000, 20000)
user1 = Usuario('Igor', 'Almeida', 'igor@gmail.com', '123456')
'''
'''
user = Usuario('Igor', 'Sobrenome', 'igor@gmail.com', '123456')
print(type('dfsdf'))
print(type(22))
print(type(user))
'''

cli1 = Cliente('Igor', '123.123.123.99')
cc = ContaCorrente(5000, 10000, cli1)
cc.mostra_cliente()
cc.cliente.diz()
