"""
POO - MRO - Method Resolution Order

MRO - a ordem de execução dos métodos, ou seja, de onde o método acessado será executado?

Pinguim(Aquatico, Terrestre)
-> Eu sou Ping do mar

Pinguim(Terrestre, Aquatico)
-> Eu sou Ping da terra

Em Python, a gente pode conferir a ordem de execução dos métodos (MRO) de 3 formas:
    - Via propriedade da classe __mro__
    - Via método mro()
    - Via help
-------------------------------------------
Pinguim(Aquatico, Terrestre)

Pinguim.__mro__

(<class '__main__.Pinguim'>, <class '__main__.Aquatico'>, <class '__main__.Terrestre'>,
<class '__main__.Animal'>, <class 'object'>)

Um método sendo executado será buscado primeiramente em Pinguim, se ele não estiver definido, será buscado em
Aquatico, seguido por Terrestre, depois em Animal e por fim em object. O primeiro que encontrar será executado
e os outros de classes mais genéricas serão ignorados.

"""


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


class Pinguim(Aquatico, Terrestre):

    def __init__(self, nome):
        super().__init__(nome)


pinguim = Pinguim('Ping')
print(pinguim.cumprimentar())  # ????? Method Resolution Order - MRO
print(Pinguim.__mro__)

help(Pinguim)









