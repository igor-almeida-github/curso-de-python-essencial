"""
Conhecendo o Pickle

A função do Pickle é realizar o seguinte processo:

Objeto Python -> Binarização
Binarização -> Objeto Python

Este processo é chamado de serialização/deserialização

# OBS: O módulo Pickle não e seguro contra dados maliciosos e desta forma não é recomendado trabalhar com arquivos
pickle vindo de outras pessoas que você não conheça ou de fontes desconhecidas.
"""
import pickle


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def comer(self):
        print(f'{self.__nome} está comendo...')

    @property
    def nome(self):
        return self.__nome


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.nome} está miando...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self.nome} está latindo...')


# felix = Gato('Felix')
# pluto = Cachorro('Pluto')
#
# with open('animais.pickle', 'wb') as arquivo:
#     pickle.dump((felix, pluto), arquivo)


with open('animais.pickle', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)

print(f'O gato chama-se {gato.nome}')
gato.mia()
print(f'O cachorro chama-se {cachorro.nome}')
cachorro.late()

