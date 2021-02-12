"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo string

Em python, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos
- Aspas simples -> 'angelina'
- Aspas duplas -> "angelina"
- Aspas simples triplas -> '''angelina'''
"""
# - Aspas duplas triplas -> """angelina"""

# Entrada de dados
# print("Qual seu nome? ")
# nome = input()

nome = input('Qual seu nome? ')

# Exemplo de print 'antigo' 2.x
# print("Seja bem vindo(a) %s" % nome)

# Exemplo de print 'moderno' 3.x
# print('Seja Bem Vindo(a) {0}'.format(nome))

# Exemplo de print 'mais atual' 3.7
print(f"Seja Bem-vindo {nome}")

# print("Qual sua idade? ")
# idade = input()

idade = int(input('Qual sua idade? '))

# Processamento

# Saída de dados
# Exemplo de print 'antigo' 2.x
# print("O %s tem %s anos" % (nome, idade))

# Exemplo de print 'moderno' 3.x
# print('O {0} tem {1} anos'.format(nome, idade))

# Exemplo de print 'mais atual' 3.7
print(f'O {nome} tem {idade} anos')

# int(idade) => Cast: é a 'conversão' de um tipo de dado para outro.
print(f'O {nome} nasceu em {2019 - idade}')

