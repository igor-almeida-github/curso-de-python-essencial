"""
Tipo String:

Em Python um dado é considerado do tipo string sempre que:

- Estiver entre aspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre aspas duplas -> "uma string", "234", "a", "True", "42.3"
- Estiver entre aspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''
"""
# - Estiver entre aspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""
"""
# Printando string
nome = 'Geek university'
print(nome)
print(type(nome))

# Como printar com ' no meio do texto
nome = "Ginas's Bar" 
print(nome)
print(type(nome))

# Saltar linha no meio do print
nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

# Outra forma de printar ' no meio do texto
nome = 'Angelina \' Jolie'
print(nome)
print(type(nome))

# Outra forma de saltar linhas
nome = '''Angelina
Jolie'''
print(nome)
print(type(nome))

# Printando tudo em caixa alta ou caixa baixa
nome = Python
print(nome.upper())
print(nome.lower())

# Cria um lista de strings com os elementos da string separados por espaço ou salto de linha
nome = 'python GUI\nola'
print(nome.split())

nome = 'python GUI'
# Na verdade é:
# [0,    1,   2,   3,   4,   5,   6,   7,   8,   9]
# ['p', 'y', 't', 'h', 'o', 'n', ' ', 'G', 'U', 'I']

# Printa phyton, de 0 até 5, (6 é o limite que não chega, quando é colocado a:n ele pega de a até n-1)
nome = 'python GUI' 
print(nome[0:6]) # Slice de string

# Printa o primeiro nome, primeiro cria uma lista contendo ['python', 'GUI'] e depois pega só o primeiro elemento
nome = 'python GUI'
print(nome.split()[0])

# Indexação:
['python', 'GUI']
[    0,      1  ]

# [::-1] comece do primeiro elemento, vá até o último elemento e inverta
nome = 'python GUI'
print(nome[::-1])

# substitui um caracter por outro na string (primeiro pelo segundo)
nome = 'python GUI'
print(nome.replace(' ', ''))
"""


