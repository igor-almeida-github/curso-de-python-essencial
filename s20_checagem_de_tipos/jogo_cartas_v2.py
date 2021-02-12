import random
from typing import List, Tuple, Dict

naipes: List[str] = '♠ ♡ ♢ ♣'.split()
cartas: List[str] = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


def criar_baralho(aleatorio: bool = False) -> List[Tuple[str, str]]:
    """Cria um baralho com 52 cartas"""
    baralho: List[Tuple[str, str]] = [(n, c) for c in cartas for n in naipes]
    if aleatorio:
        random.shuffle(baralho)
    return baralho


def distribuir_cartas(baralho: List[Tuple[str, str]]) -> Tuple[List[Tuple[str, str]], List[Tuple[str, str]],
                                                               List[Tuple[str, str]], List[Tuple[str, str]]]:
    """Gerencia a mão de cartas de acordo com o baralho gerado"""
    return baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4]


def jogar():
    """Inicia um jogo de cartas para 4 jogadores"""
    baralho: List[Tuple[str, str]] = criar_baralho(aleatorio=True)
    jogadores: List[str] = 'P1 P2 P3 P4'.split()
    maos: dict = {jogador: mao for jogador, mao in zip(jogadores, distribuir_cartas(baralho))}
    print(maos)

    for jogador in jogadores:
        print(f'{jogador}: ' + ' '.join([f'{naipe}{carta}' for naipe, carta in maos[jogador]]))


if __name__ == '__main__':
    jogar()
