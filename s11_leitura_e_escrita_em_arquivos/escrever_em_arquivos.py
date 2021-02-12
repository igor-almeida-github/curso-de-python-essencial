"""
Escrevendo em arquivos

OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele, apenas ler.
Da mesmo forma, se abrirmos um arquivo para escrita, não podemos lê-lo, somente escrever nele.

OBS: Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional.

Para escrever em um arquivo, após abrir o arquivo, utilizamos a função write().
Esta função recebe uma string como parâmetro, caso contrário teremos um TypeError.

Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir será criado.
Caso ele já exista, o anterior será apagado e um novo será criado. Dessa forma, todo
o conteúdo no arquivo anterior é perdido.

"""

# Exemplo de escrita - modo 'w' - write
'''
with open('novo.txt', 'w', encoding='UTF-8') as arquivo:
    arquivo.write('Escrever dados em arquivo é muito fácil.\n')
    arquivo.write('Podemos colocar quanta linhas quisermos.\n')
'''
# Forma não Pythônica de abrir um arquivo para a escrita
'''
arquivo = open('novo.txt', 'w', encoding='UTF-8')
arquivo.write('Escrevendo dados no arquivo de forma não Pythônica.')
arquivo.close()
'''
# Exemplo 3
'''
with open('geek.txt', 'w', encoding='UTF-') as arquivo:
    arquivo.write(('geek '*10 + '\n')*100)
'''
# Exemplo 4
'''
with open('frutas.txt', 'w', encoding='UTF-8') as arquivo:
    while True:
        fruta = input('Digite uma fruta ou digite sair: ')
        if fruta == 'sair':
            break
        arquivo.write(fruta + '\n')
'''

