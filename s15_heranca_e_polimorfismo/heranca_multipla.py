"""
POO - Herança Múltipla

Herança Múltipla nada mais é do que a possibilidade de uma classe herdar de mútiplas classes,
fazendo com que a classe filha herde todos os atributos e métodos de todas as classes herdadas.

# OBS: A herança múltipla pode ser feita de duas maneiras:
    - Por Multiderivação Direta;
    - Por Multiderivação Indireta;

# Não importa se a derivação é direta ou indireta. A classe que realizar a herança, herda todos os
seus atributos e métodos da superclasse.

Toda classe criada em Python herda de object
"""


# Exemplo 1 - Multiderivação Direta
'''
class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class MultiDerivada(Base1, Base2, Base3):
    pass
'''


# Exemplo 2 - Multiderivação Indireta
'''
class Base1:
    pass


class Base2(Base1):
    pass


class Multiderivada(Base2):
    pass
'''


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._Animal__nome} está nadando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self._Animal__nome} está adando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra'


class Pinguim(Aquatico, Terrestre):  # Método cumprimentar vem do Aquatico, pois ele aparece primeiro.

    def __init__(self, nome):
        super().__init__(nome)


baleia = Aquatico('Baleia')
print(baleia.nadar())
print(baleia.cumprimentar())
print('---------------------------')

gato = Terrestre('Gato')
print(gato.andar())
print(gato.cumprimentar())
print('---------------------------')

pinguim = Pinguim('Ping')
print(pinguim.nadar())
print(pinguim.andar())
print(pinguim.cumprimentar())  # ????? Method Resolution Order - MRO
print('---------------------------')


# Objeto é instância de ...
print(f'pinguim é instância de Pinguim? {isinstance(pinguim, Pinguim)}')
print(f'pinguim é instância de Aquatico? {isinstance(pinguim, Aquatico)}')
print(f'pinguim é instância de Terrestre? {isinstance(pinguim, Terrestre)}')
print(f'pinguim é instância de Animal? {isinstance(pinguim, Animal)}')
print(f'pinguim é instância de object? {isinstance(pinguim, object)}')

# O que é herdado de object? Veja...
print(dir(object))
