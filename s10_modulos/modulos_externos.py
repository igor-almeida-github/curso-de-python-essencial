"""
Módulos Externos

Utilizamos o gerenciador de pacotes Python chamado Pip - Python Installer Package
VOcê pode conhecer todos os pacotes externos oficiais em: https://pypi.org

colorama -> É utilizado para permitir impressão e textos coloridos no terminal
pip install colorama

Instalando um módulo:

pip install nome_do_módulo (mas é melhor olhar no site, lá já diz o comando para instalar)

"""
'''
from colorama import (init, Fore, Back, Style)
init()
print(Fore.RED + 'Igor Almeida' + Fore.BLUE + ' gosta de' + Fore.YELLOW + ' Python')
print(Style.RESET_ALL, end='')
print(Fore.BLACK + Back.RED + 'Geek university')
print(Style.RESET_ALL, end='')
print('Igor')
'''














