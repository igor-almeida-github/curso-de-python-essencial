import math

'''
def circunferencia(raio: float) -> float:
    return 2 * math.pi * raio


print(circunferencia.__annotations__)


nome: str = 'Geek University'
peso: float = 67.9
ativo: bool = True

print(nome)
print(peso)
print(ativo)

print(__annotations__)
'''


class Pessoa:

    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso

    def andar(self) -> str:
        return f'{self.__nome} está andando'


pessoa = Pessoa('Igor', 24, 77.4)

print(pessoa.__dict__)
print(pessoa.andar.__annotations__)
print(pessoa.__init__.__annotations__)



