"""
Seek e Cursors

seek() -> É utilizada para movimentar o cursor pelo arquivo. Ela recebe um parâmetro que indica onde
queremos colocar o cursor.

OBS: Quando abrimos um arquivo com a função open(), é criada uma conexão entre o arquivo no disco do computador
e o nosso programa. Essa conexão é chamada de streaming. Ao finalizar os trabalhos com o arquivo, devemos
fechar essa conexão. Para isso utilizamos a função close().

Passos para se trabalhar com um arquivo:
1 - Abrir o arquivo;
2 - Trabalhar com o arquivo;
3 - Fechar o arquivo;
"""
# Exemplo antigo, sem controlar o cursor
'''
arquivo = open('C:\\Users\\igor_\\Desktop\\python_arq\\python_txt.txt', encoding='UTF-8')
print(arquivo.read())
print(arquivo.read())  # Não imprime nada
'''
# Movimentando o cursor pelo arquivo com a função seek()
'''
arquivo = open('C:\\Users\\igor_\\Desktop\\python_arq\\python_txt.txt', encoding='UTF-8')
print(arquivo.read())
arquivo.seek(0)
print(arquivo.read())
'''
# readline() -> Função que lê o arquivo linha a linha
'''
arquivo = open('C:\\Users\\igor_\\Desktop\\python_arq\\python_txt.txt', encoding='UTF-8')
print(arquivo.readline(), end='')
print(arquivo.readline(), end='')
print(arquivo.readline(), end='')
print(arquivo.readline(), end='')
'''
# Tipo de retorno de readline()
'''
arquivo = open('C:\\Users\\igor_\\Desktop\\python_arq\\python_txt.txt', encoding='UTF-8')
print(type(arquivo.readline()))  # 'str'
'''
# readlines() -> Lendo todas as linhas e armazenando em um lista, em que cada elemento é uma str contendo uma linha.
'''
arquivo = open('C:\\Users\\igor_\\Desktop\\python_arq\\python_txt.txt', encoding='UTF-8')
print(arquivo.readlines())
'''
# Fechando o arquivo com o close() - Rodar no terminal para verificar que o arquivo não pode ser deletado enquanto
# não damos arquivo.close()
'''
arquivo = open('C:\\Users\\igor_\\Desktop\\python_arq\\python_txt.txt', encoding='UTF-8')
print(arquivo.closed)  # Verifica se o arquivo está aberto ou fechado
arquivo.close()
print(arquivo.closed)
# print(arquivo.read())  # ValueError
# OBS: Se tentarmos manipular o arquivo após seu fechamento, teremos um ValueError
'''
# É possivel limitar a quantidade de caracteres a serem lidos no arquivo.
'''
arquivo = open('C:\\Users\\igor_\\Desktop\\python_arq\\python_txt.txt', encoding='UTF-8')
print(arquivo.read(10))
'''

