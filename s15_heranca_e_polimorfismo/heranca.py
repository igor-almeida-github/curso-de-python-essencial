"""
POO - Herança (Inheritance)

A ideia de herança é a de reaproveitar código. Também extender nossas classes.
OBS: Com a herança, a partir de uma classe existente, nós extendemos outra classe que passa a herdar atributos
e métodos da classe herdada.

Cliente
    - nome;
    - sobrenome;
    - cpf;
    - renda;

Funcionario
    - nome;
    - sobrenome
    - cpf;
    - matricula;

Pergunta: Existe alguma entidade genérica o suficiente para encapsular os atributos e métodos comuns a essas entidades?

OBS: Quando uma classe herda de outra classe ela herda TODOS os atributos e métodos da classe herdada.

Quando uma classe herda de outra classe, a classe herdada é conhecida por:
    [Pessoa]
    - Super Classe;
    - Classe Mãe;
    - Classe Pai;
    - Classe Base;
    - Classe Genérica;

Quando uma classe herda de outra classe, ela é chamada:
    [Cliente, Funcionario]
    - Sub Classe;
    - Classe Filha;
    - Classe Específica;

Sobrescrita de Métodos - ocorre quando reescrevemos um método presente na superclasse em classes filhas.
"""

# Forma repetitiva
'''
class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


cliente1 = Cliente('Igor', 'Almeida', '12345678900', 1300)
funcionario1 = Funcionario('Angelina', 'Jolie', '37788829032', 57664)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
'''


# Herança
'''
class Pessoa:
    def __init__(self,  nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    """Cliente herda de Pessoa"""
    def __init__(self,  nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionario herda de Pessoa"""
    def __init__(self,  nome, sobrenome, cpf, matricula):
        # super().__init__(nome, sobrenome, cpf)  # Forma comum
        Pessoa.__init__(self, nome, sobrenome, cpf)  # Forma não comum de acessar dados da super classe
        self.__matricula = matricula


cliente1 = Cliente('Igor', 'Almeida', '09923948641', 1300)
funcionario1 = Funcionario('Angelina', 'Jolie', '37788829032', 57664)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
print(cliente1.__dict__)
print(funcionario1.__dict__)
'''


# Sobrescrita de Métodos (Overriding)
class Pessoa:
    def __init__(self,  nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    """Cliente herda de Pessoa"""
    def __init__(self,  nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    """Funcionario herda de Pessoa"""
    def __init__(self,  nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self._Pessoa__nome} {self.__matricula}'


cliente1 = Cliente('Igor', 'Almeida', '09923948641', 1300)
funcionario1 = Funcionario('Angelina', 'Jolie', '37788829032', 57664)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())


