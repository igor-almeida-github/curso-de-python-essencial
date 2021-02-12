"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hieráquico utilizando classes.

Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos privados
de usuário.

"""


class Conta:

    __contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.__contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.__contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com o limite de {self.__limite}')

    def depositar(self, valor):
        if valor < 0:
            raise ValueError('O valor informado deve ser maior ou igual a zero.')
        self.__saldo += valor

    def sacar(self, valor):
        if valor < 0:
            raise ValueError('O valor informado deve ser maior ou igual a zero.')
        if valor > self.__saldo:
            print('Não há saldo suficiente para o saque.')
        else:
            self.__saldo -= valor

    def transferencia(self, valor, destino):
        if self.__saldo >= valor:
            self.sacar(valor)
            destino.depositar(valor)
        else:
            print('Não há saldo suficiente para a transferência')


# Testando

conta1 = Conta('Igor', 150, 1500)
conta2 = Conta('Almeida', 400, 2000)
'''
print(conta1.__dict__)
conta1.extrato()
conta1.depositar(150)
conta1.extrato()
conta1.sacar(50)
conta1.extrato()
conta1.sacar(260)
conta1.extrato()
'''
# Transferência, forma 1
'''
conta1.extrato()
conta2.extrato()

value = 100
conta2.sacar(value)
conta1.depositar(value)

conta1.extrato()
conta2.extrato()
'''
# Transferência, forma 2
conta1.extrato()
conta2.extrato()
conta2.transferencia(100, conta1)
conta1.extrato()
conta2.extrato()


