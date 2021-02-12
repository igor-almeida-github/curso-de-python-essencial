"""
Sistema de Arquivos - Manipulação

https://docs.python.org/3/library/os.html
"""
import os
import stat
import shutil
from send2trash import send2trash
import tempfile
# Descobrindo se um arquivo ou diretório existe
'''
# Arquivo
print(os.path.exists('arquivo.txt'))  # False
print(os.path.exists('frutas.txt'))  # True
# Diretório
print(os.path.exists('geek'))  # True
print(os.path.exists('geek\\university'))  # True
print(os.path.exists('playstation'))  # False
print(os.path.exists('C:\\Users\\igor_\\Desktop\\workspace\\sistema'))  # True
'''
# Criando arquivos
'''
# Forma 1
open('arquivo-teste.txt', 'w', encoding='UTF-8').close()
# Forma 2
open('arquivo-teste2.txt', 'a', encoding='UTF-8').close()
# Forma 3
with open('C:\\Users\\igor_\\Desktop\\workspace\\sistema\\arquivo-teste3.txt', 'w', encoding='UTF-8'):
    pass
'''
# Criando diretórios com mkdir
'''
os.mkdir('C:\\Users\\igor_\\Desktop\\workspace')  # Se já existir, então teremos FileExistsError
# OBS: se não tivermos permissão para criar o diretório teremos um PermissionError
'''
'''
os.mkdir('playstation\\playstation2')  # Erro FileNotFoundError, não é possível criar um diretório dentro de outro
# que ainda não existe, ou seja, os diretórios não são criados simultaneamente. Com o mkdir é
# possível criar apenas um único de cada vez.
'''
# Criando múltiplos diretórios com mkdirs (árvore)
'''
os.makedirs('playstation\\playstation2\\playstation3')  # Cria todos simultaneamente
# OBS: Se TODOS já existirem, dará erro. Se pelo menos 1 não existir, ele será criado normalmente, sem erros.
'''
'''
os.makedirs('python1\\python2\\python3', exist_ok=True)  # Cria múltiplos diretórios e se todos já existirem, não
# é apresentado erro, ao invés disso, o comando é ignorado. (não cria de novo)
'''
# Renomeando diretórios ou arquivos (mesma coisa)
'''
os.rename('C:\\Users\\igor_\\Desktop\\workspace\\sistema\\texto.txt',
          'C:\\Users\\igor_\\Desktop\\workspace\\sistema\\textoNovo.txt')
# OBS: Se o diretório ou arquivo não existir, teremos um FileNotFoundError
'''
# Deletar ARQUIVOS (somente)
'''
# OBS: ATENÇÃO! Tome cuidado com os comandos de deleção. Ao deletarmos um arquivo ou diretório,
# eles não vão para a lixeira. Eles somem.
os.remove('C:\\Users\\igor_\\Desktop\\workspace\\sistema\\texto.txt')
# OBS: Se você estiver no Windows e o arquivo que você for deletar estiver em uso, você terá um erro.
# OBS: Caso o arquivo não exista, teremos o FileNotFoundError
# OBS: Se você informar um diretório ao invés de um arquivo, teremos um Erro.
'''
# Removendo diretórios vazios únicos
'''
os.rmdir('C:\\Users\\igor_\\Desktop\\workspace\\sistema')  # OSError -> A pasta não está vazia
# OBS: Se o diretório tiver conteudo, teremos um erro.
# Se o diretório não existir teremos um Erro.
'''
# Removendo uma arvore de diretórios (solução própria)
'''
diretorio_para_excluir = 'C:\\Users\\igor_\\Desktop\\workspace'
caminho = diretorio_para_excluir
try:
    os.rmdir(diretorio_para_excluir)
except OSError:
    while os.path.exists(diretorio_para_excluir):
        conteudo = list(os.scandir(caminho))
        diretorios_dentro = list(filter(lambda x: x.is_dir(), conteudo))
        if len(diretorios_dentro) == 0:
            arquivos_dentro = list(filter(lambda x: x.is_file(), conteudo))
            for arquivo in arquivos_dentro:
                os.remove(arquivo.path)
            os.rmdir(caminho)
            caminho = os.path.join(caminho, '..')
        else:
            caminho = diretorios_dentro[0].path
'''
# Podemos remover um ramo de uma arvore de diretórios vazio (pastas sem arquivos)
# Se algum dos diretórios contiver arquivos ou outros diretórios, o processo para.
'''
os.removedirs('C:\\Users\\igor_\\Desktop\\workspace\\Nova pasta (2)\\Nova pasta')
'''
# Podemos remover recursivamente um diretório incluindo seu conteúdo com rmtree()
'''
shutil.rmtree('C:\\Users\\igor_\\Desktop\\workspace')
'''
# Podemos enviar um arquivo para a lixeira. (ao contrário das formas vistas anteriormente,
# que deletavam permanentemente). Se arquivo não existir -> OSError
'''
send2trash('C:\\Users\\igor_\\Desktop\\workspace')
'''
# Criando diretórios temporários
'''
with tempfile.TemporaryDirectory() as tmp:
    print(f'criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporário.txt'), 'w', encoding='UTF-8') as arquivo:
        arquivo.write('Igor Almeida')
    input()
# Estamos criando um diretório temporário, abrindo o mesmo e dentro dele criando um arquivo para escrevermos um texto.
# No final, usamos um input() só para mantermos os arquivos temporários "vivos" dentro dos blocos with.
'''
# Criando um arquivo temporário
'''
with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University\n')
    tmp.seek(0)
    print(tmp.read())
# OBS: Em arquivos temporários só conseguimos escrever bits. Por isso, utilizamos b''
'''
# Outra forma
'''
arquivo = tempfile.TemporaryFile()
arquivo.write(b'Igor')
arquivo.close()
'''
'''
arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Igor')
print(arquivo.name)
arquivo.seek(0)
print(arquivo.read())
input()
arquivo.close()
'''


