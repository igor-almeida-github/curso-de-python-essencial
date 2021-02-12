"""
Lendo arquivos CSV

CSV - Comma Separated Values

# Separador por vírgula

1, 2, 3, 4, 5, 6

"geek", "university", "python"

# Separador por ponto e vírgula

1; 2; 3; 4; 5; 6

"geek"; "university"; "python"

# Separador por espaço

1 2 3 4 5 6

"geek" "university" "python"

A linguagem Python possui duas formas diferentes para ler dados em arquivos CSV:
    - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
    - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts;

"""
from csv import reader, DictReader

# Forma possivel de se trabalhar, mas não é o ideal (trabalhoso)
'''
with open('lutadores.csv', encoding='UTF-8') as arquivo:
    dados = arquivo.read()
    # print(type(dados))
    linhas = dados.split('\n')
    dados = [tuple(linha.split(',')) for linha in linhas][1:]
    print(dados)
'''

# Reader
'''
with open('lutadores.csv', encoding='UTF-8') as arquivo:
    leitor_csv = reader(arquivo)
    print(type(leitor_csv))
    next(leitor_csv)
    for linha in leitor_csv:
        print(f'{linha[0]}  nasceu no(a)(s) {linha[1]} e mede {linha[2]} cm.')
'''

# DictReader
'''
with open('lutadores.csv', encoding='UTF-8') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']} cm")
'''
# DictReader com outro separador
with open('lutadores.csv', encoding='UTF-8') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')
    print(leitor_csv)
    for linha in leitor_csv:
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']} cm")



