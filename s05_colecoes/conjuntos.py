"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência a teoria dos conjuntos da matemática.

- Aqui no python, on conjuntos são chamados de sets.

Dito isso, da mesma forma que na matemática:
- Sets, ou seja conjuntos, não possuem valores duplicados.
- Sets, não possuem valores ordenados.
- Elementos não são acessados via índice, ou seja, conjuntos não são idexados.

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas
não nos importamos com a ordenação deles. Quando não precisamos nos preocupar com
chaves, valores e itens duplicados.

Os conjuntos (sets) são referênciados em python com chaves {}

Diferença entre conjuntos(sets) e mapas(dicionários) em Python:
- Um dicionário tem chave valor.
- Um conjunto tem apenas valor.
"""


# Definindo um conjunto:
'''
# Forma 1
s = set({1, 4, 'e32', None, (1, 2), 1.222, -9, 4, 4, 4})  # Repare que  temos valores repetidos
print(s)
print(type(s))
# OBS: ao criar um conjunto, caso sejam adicionados valores repetidos, serão ignorados sem gerar erro

# Forma 2 (mais comum)
s = {1, 4, 'e32', None, (1, 2), 1.222, -9, 4, 4, 4}
print(s)
print(type(s))
'''


# Podemos verificar se determinado elemento está contido no conjunto
'''
s = {1, 4, 'e32', None, (1, 2), 1.222, -9, 4, 4, 4}
if 4 in s:
    print('Tem o 4')
else:
    print('Não tem o 4')
'''


# Importante lembrar que além de não termos valores duplicados, não temos ordem em sets
'''
lista = [99, 1, 22, 655, 22, 0, -1]  # Em lista temos ordem e valores duplicados
s = set(lista)  # Já sets não
print(lista)
print(s)
'''


# Assim como todo outro conjunto Python, podemos colocar todo tipo de dados misturados em sets, exceto listas,
# sets, dicionários.
'''
s = {1, 4, 'e32', None, (1, 2), 1.222, -9, 4, 4, 4}
print(s)
'''


# Podemos iterar em um set normalmente
'''
s = {1, 4, 'e32', None, (1, 2), 1.222, -9, 4, 4, 4}
print(s)
for valor in s:
    print(valor)
'''


# Usos interessantes com sets
'''
# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu, e os visitantes
# informaram manualmente a cidade de onde vieram. Nós adicionamos cada cidade em uma lista Python
# já que em uma lista podemos adicionar novos elementos e ter repetição.

cidades = ['ervália', 'viçosa', 'ubá', 'nova york', 'ubá', 'viçosa', 'viçosa']
print(cidades)
print(len(cidades))  # Quantas pessoas visitaram o museu?

# Agora precisamos saber quantas cidades diferentes as pessoas são
print(len(set(cidades)))  # Podemos usar o set para isso
'''


# Adicionando elementos em um conjunto
'''
s = {1, 2, 3}
print(s)
s.add(4)
s.add(4)  # Não duplicará, simplesmente será ignorado
print(s)
# OBS: conjuntos são mutáveis
'''


# Remover elementos em um conjunto
'''
# Forma 1
s = {1, 2, 3}
print(s)
s.remove(2)  # Se o valor que tentamos remover não existir, será retornado keyerror
print(s)
# Forma 2
s = {1, 2, 3}
s.discard(2)  # Se o valor que tentamos remover não existir, simplesmente nada ocorrerá, não será dado erro
print(s)
'''


# Copiando um conjunto para outro
'''
# Shallow copy
s = {1, 2, 3}
s2 = s
print(s, s2)
s2.discard(2)
print(s, s2)

# Deep Copy
s = {1, 2, 3}
s2 = s.copy()
print(s, s2)
s2.discard(2)
print(s, s2)
'''


# Podemos remover todos os elementos de um conjunto
'''
s = {1, 2, 3}
print(s)
s.clear()
print(s)
'''


# Métodos matemáticos de conjuntos

# União
'''
# Imagine que temos dois conjuntos, um contendo estudantes do curso Python e outro contendo estudantes do curso Java
estudantes_python = {'Marcos', 'Patricia', 'Helen', 'Pedro', 'Júlia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Júlia', 'Ana', 'Patricia'}
# Veja que alguns alunos que estudam Python também estudam Java
# Precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1 - Utilizando union (união entre conjuntos)
unicos1 = estudantes_java.union(estudantes_python)
print(unicos1)

# Forma 2 - Utilizando o caractere pipe |
unicos2 = estudantes_python | estudantes_java
print(unicos2)
'''


# Interseção
'''
estudantes_python = {'Marcos', 'Patricia', 'Helen', 'Pedro', 'Júlia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Júlia', 'Ana', 'Patricia'}

# Forma 1 - Utilizando intersection
ambos1 = estudantes_java.intersection(estudantes_python)
print(ambos1)

# Forma 2 - Utilizando o caractere &
ambos2 = estudantes_java & estudantes_python
print(ambos2)
'''


# Gerar um conjunto de estudantes de um curso que não estão no outro
'''
estudantes_python = {'Marcos', 'Patricia', 'Helen', 'Pedro', 'Júlia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Júlia', 'Ana', 'Patricia'}

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)
'''

# Soma*, Valor máximo*, Valor mínimo*, Tamanho
# OBS: se os valores forem inteiros/reais
'''
s = {1, 2, 3, 4, 5, 6}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))
'''
