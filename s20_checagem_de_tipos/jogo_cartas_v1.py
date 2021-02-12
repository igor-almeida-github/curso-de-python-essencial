"""
nomes: list = ['igor', 'almeida']
versoes: tuple = (1, 2, 3)
opcoes: dict = {'ar': True, 'bncco_couro': True}
valores: set = {3, 4, 5, 6}


print(nomes)
print(versoes)
print(opcoes)
print(valores)
print(__annotations__)

class Igor:
    pass

g1: Igor = Igor()
"""
"""
from typing import Dict, List, Tuple, Set


nomes: List[str] = ['Geek', 'university']
versoes: Tuple[int, int, int] = (1, 2, 3)
opcoes: Dict[str, bool] = {'ar': True, 'banco_couro': True}
valores: Set[int] = {3, 4, 5, 6}

print(nomes)
print(versoes)
print(opcoes)
print(valores)
print(__annotations__)
"""
import random

naipes = '♠ ♡ ♢ ♣'.split()
cartas = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


def criar_baralho(aleatorio=False):
    """Cria um baralho com 52 cartas"""
    baralho = [(n, c) for c in cartas for n in naipes]
    if aleatorio:
        random.shuffle(baralho)
    return baralho


def distribuir_cartas(__baralho):
    """Gerencia a mão de cartas de acordo com o baralho gerado"""
    return __baralho[0::4], __baralho[1::4], __baralho[2::4], __baralho[3::4]


# print(naipes)
# print(cartas)
# print(criar_baralho())
#
# baralho = criar_baralho()
# print(distribuir_cartas(baralho))

def jogar():
    """Inicia um jogo de cartas para 4 jogadores"""
    baralho = criar_baralho(aleatorio=True)
    jogadores = 'P1 P2 P3 P4'.split()
    maos = {jogador: mao for jogador, mao in zip(jogadores, distribuir_cartas(baralho))}

    for jogador in jogadores:
        print(f'{jogador}: ' + ' '.join([f'{naipe}{carta}' for (naipe, carta) in maos[jogador]]))


if __name__ == '__main__':
    jogar()

