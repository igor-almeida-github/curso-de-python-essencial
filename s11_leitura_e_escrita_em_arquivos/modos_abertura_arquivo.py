"""
Modos de Abertura de Arquivo

r -> Abre para a leitura - padrão
w -> Abre para a escrita - sobrescreve caso o arquivo já exista
x -> Abre para escrita somente se o arquivo não existir. Caso o arquivo exista, gera FileExistsError.
a -> Abre para a escrita, adicionando no final do arquivo se existir.
+ -> Abre para o modo de atualização: Leitura e Escrita. (temos o controle do cursor)

OBS: Abrindo no modo 'a' -> append, se o arquivo não existir será criado. Caso exista,
o novo conteúdo será adicionado SEMPRE ao final do arquivo. Com o modo 'a', não controlamos o cursor.

http://docs.python.org/3/library/functions.html#open
"""
# Exemplo do 'x'
'''
try:
    with open('university.txt', 'x', encoding='UTF-8') as arquivo:
        arquivo.write('Teste de conteúdo.\n')
except FileExistsError:
    print('Arquivo já existe')
'''
# Exemplo do 'a'
'''
with open('frutas.txt', 'a', encoding='UTF-8') as arquivo:
    while True:
        fruta = input('Informe um fruta ou sair: ')
        if fruta == 'sair':
            break
        arquivo.write(fruta + '\n')
'''
# Adicionando no início
'''
with open('texto.txt', 'r+', encoding='UTF-8') as arquivo:
    texto_anterior = arquivo.read()
    arquivo.seek(0)
    arquivo.write('Novo texto 33333' + '\n' + texto_anterior)
'''



