"""
Sistema de Arquivos e Navegação.

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer uso do módulo os.
os -> Operating System - Sistema Operacional
"""
import os
import platform
import sys
'''
# getcwd() -> pega o current work directory - diretório de trabalho atual
# Retorna o path (caminho) absoluto
print(os.getcwd())
# Para mudar o diretório podemos utilizar o chdir()

os.chdir('C:\\Users\\igor_\\Desktop')
for i in range(50):
    arquivo = open(f'sabotagem{i}.txt', 'w', encoding='UTF-8')
    arquivo.write('sua area de trabalho está cheia\n'*100)
    arquivo.close()
'''
# Voltando diretórios até encontrar área de trabalho
'''
while True:
    if 'Desktop' in os.listdir() or 'Área de Trabalho' in os.listdir():
        break
    os.chdir('..')
    print(os.getcwd())
'''
# Voltando diretórios até encontrar a raiz
'''
while os.getcwd() != 'C:\\':
    os.chdir('..')
    print(os.getcwd())
'''
# Podemos checar se um diretório é absoluto ou relativo
'''
print(os.path.isabs('igor_\\PycharmProjects'))
print(os.path.isabs('C:\\Users\\igor_\\PycharmProjects'))
'''
# Podemos identificar o sistema operacional com o módulo os
'''
print(os.name)  # posix (linux e Mac), nt (Windows)
# Podemos ter mais detalhes no sistema operacional
print(platform.uname())
print(sys.platform)
'''
# Podemos criar diretórios
'''
os.chdir('C:\\Users\\igor_\\Desktop')
try:
    os.mkdir('workspace')
    os.mkdir('workspace\\sistema')
except FileExistsError:
    try:
        os.mkdir('workspace\\sistema')
    except FileExistsError:
        pass

# Forma de acesso
print(os.getcwd())
os.chdir('workspace')
print(os.getcwd())
os.chdir('..')  # Volta

# Outra forma - O os.path.join() recebe parâmetros e junta com a
# separação correta de acordo com o sistema operacional.
print(os.getcwd())
path = os.path.join(os.getcwd(), 'workspace', 'sistema')  # Independente do sistema operacional
os.chdir(path)
print(os.getcwd())
'''
# Podemos listar os arquivos e diretórios com o listdir()
'''
print(os.listdir())
'''
# Podemos listar os arquivos e diretórios com mais detalhes com o scandir()
with os.scandir() as scanner:
    arquivos = list(scanner)
    print(arquivos)
    print(dir(arquivos[1]))
    print(arquivos[1].name)  # Nome
    print(arquivos[1].inode())  # ??
    print(arquivos[1].is_dir())  # É diretório?
    print(arquivos[1].is_file())  # É arquivo?
    print(arquivos[1].is_symlink())  # É link simbólico
    print(arquivos[1].path)  # Caminho até o arquivo
    print(arquivos[1].stat())  # Estatísticas

# OBS: Quando utilizamos a função scandir() nós precisamos fechá-la, assim como quando
# abrimos um arquivo, aqui usamos o with, que fecha o contexto sozinho no final.






