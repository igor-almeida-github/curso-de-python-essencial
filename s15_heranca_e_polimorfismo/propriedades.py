"""
POO - Propriedades (Properties)

Em linguagens de programação como o Java, ao declararmos atributos privados nas classes, costumamos a criar
métodos públicos para manipulação desses atributos. Esse métodos são conhecidos por getters e setters.
Onde os getters retornam o valor do atributo e os setters modificam o valor do mesmo.


"""


# Forma tradicional de outras linguagens
'''
class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        Conta.contador += 1
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

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

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, valor):
        self.__saldo = valor

    def get_limite(self):
        return self.__limite


conta1 = Conta('Carlos', 10_000, 78_000)
conta2 = Conta('Felicity', 300_000, 1_000_000)

conta1.extrato()
conta2.extrato()

print(f'A soma dos saldos das contas é {conta1.get_saldo() + conta2.get_saldo()}')

conta1.set_saldo(1_000_000)
conta1.extrato()
'''


# Utilizando propriedades
class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        Conta.contador += 1
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property  # com @property - > conta1.numero   //  sem @property -> conta1.numero()
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @property
    def valor_total(self):
        return self.__saldo + self.__limite

    @saldo.setter
    def saldo(self, novo_saldo):
        self.__saldo = novo_saldo

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


conta1 = Conta('Carlos', 10_000, 78_000)
conta2 = Conta('Felicity', 300_000, 1_000_000)

print(conta1.saldo)
print(conta2.saldo)
print(conta1.valor_total)

conta1.saldo = 90
conta2.saldo = 90

print(conta1.saldo)
print(conta2.saldo)
