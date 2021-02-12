"""
Leitura de Arquivos

Para ler o conteúdo de um arquivo em Python, utilizamos a função integrada open(), que literalmente significa 'abrir'.
open() -> Na forma mais simples de utilização nós passamos apenas um parâmetro de entrada, que neste caso é o caminho
do arquivo a ser lido. Essa função retorna um _io.TextIOWrapper e é com ele que trabalhamos então.

https://docs.python.org/3/library/functions.html#open

# OBS: Por padrão a a função open() abre o arquivo para leitura. Este arquivo deve existir, ou
então teremos o erro FIleNotFoundError.

mode r -> Modo de Leitura. r -> read() -> ler
encoding='UTF-8' -> Permite os caracteres especiais.
"""

# Referência relativa
'''
arquivo = open('texto.txt', encoding='UTF-8')
print(arquivo)
print(type(arquivo))
print(dir(arquivo))
'''
# Referência Absoluta
'''
arquivo = open('C:\\Users\\igor_\\Desktop\\python_arq\\python_txt.txt', encoding='UTF-8')
# Para ler o conteúdo de um arquivo, após sua abertura, devemos utilizar a função read()
texto = arquivo.read()
print(texto)
print(type(texto))
print(texto.split('\n'))
'''
# O Python, utiliza um recurso para trabalhar com arquivos chamado cursor. Esse cursor funciona como o cursor
# quando estamos escrevendo, ao printar a primeira vez, o cursor vai para o final.
'''
arquivo = open('C:\\Users\\igor_\\Desktop\\python_arq\\python_txt.txt', encoding='UTF-8')
print(arquivo.read())
print(arquivo.read())  # Não imprime nada dessa vez
# OBS: A função read() lê todo o conteúdo do arquivo.
'''


