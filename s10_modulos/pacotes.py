"""
Pacotes

Módulo -> É apenas um arquivo Python que pode ter diversas funções para utilizarmos;
Pacote -> É um diretório contendo uma coleção de módulos;

OBS: Nas versões 2.x do Python, um pacote Python deveria conter dentro dele um arquivo chamado __init__.py
Nas versões 3.x, não é mais obrigatória a utilização deste arquivo, mas normalmente ainda é utilizado para
manter compatibilidade
"""
# Maneiras diferente de importar dentro de um pacote.
'''
from geek import geek1, geek2
from geek.university.geek3 import funcao3
from geek.university import geek4

print(geek1.pi)
print(geek1.funcao1(1, 3))

print(geek2.curso)
print(geek2.funcao2())

print(funcao3())

print(geek4.funcao4())
'''

