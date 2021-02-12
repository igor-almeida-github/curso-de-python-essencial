"""
Tuplas (tuple)
Tuplas são bastante parecidas com listas, existem basicamente duas diferenças básicas:
- as tuplas são representadas por parêntesis ()
- as tuplas são imutáveis: ao se criar uma tuplas, ela não muda. Toda a operação em uma tupla gera uma nova tupla

* Métodos de adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutáveis.
* Tuplas também aceitam todo o tipo de dados
"""


# Operação em um tupla gera outra tupla
'''
tupla = (1, 2, 13, 44)
tupla2 = 2*tupla
print(tupla2)
print(type(tupla2))
'''


# As tuplas são representadas por (), mas veja:
'''
tupla = (1, 2, 3, 4, 'oi')
tupla2 = 9, 24, -328, 42, 5, 6
print(tupla)
print(type(tupla))
print(tupla2)
print(type(tupla2))
'''


# Tuplas com um elemento
'''
tupla3 = (3)  # Isso não é uma tupla, isso é apenas um int
print(tupla3)
print(type(tupla3))
tupla4 = (3,)  # Isso é uma tupla
print(tupla4)
print(type(tupla4))

tupla5 = 4,
print(tupla5)
print(type(tupla5))
# Conclusão: Podemos concluir que tuplas são definidas pela , e não pelo uso do parêntesis
'''


# Podemos gerar tuplas com range:
'''
tupla = tuple(range(1, 10, 2))
print(tupla)
print(type(tupla))
'''

# Desempacotamento de tupla
'''
tupla = ('Igor Almeida', 'engenharia eletrica')
nome, curso = tupla
print(nome)
print(curso)
'''


# Soma, valor máximo, mínimo e tamanho* são aplicáveis desde que os valores forem todos inteiros ou reais
# Exceto o tamanho, que é sempre aplicável
'''
tupla = 1, 2, 3, 4, 5,
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))
'''


# Concatenação de tuplas
'''
tupla1 = 1, 2, 3
tupla2 = (4, 5, 6)
tupla3 = tupla1 + tupla2
print(tupla3)
'''


# Reescrevendo a tupla
'''
tupla1 = 1, 2, 3
print(tupla1)
tupla1 = tupla1 + (1, 2, 3)
print(tupla1)
'''

# Verificar se determinado elemento está contido na tupla
'''
tupla = (1, 2, 3)
print(33 in tupla)
'''


# Iterando sobre uma tupla
'''
tupla = (1, 2, 3)
for n in tupla:
    print(n)
    
for indice, valor in enumerate(tupla):
    print(indice, valor)
'''


# Contando elementos dentro de uma tupla
'''
tupla = ('a', 'b', 'c', 'd', 'a', 'b')
print(tupla.count('a'))
'''


# Convertendo string em tupla
'''
tupla = tuple('igor goulart de almeida')
print(tupla)
'''


# Dicas na utilização de tuplas
# Devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos em uma coleção
# Ex 1:
'''
meses = 'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
'novembro', 'dezembro'
print(meses)
# O acesso de elementos em uma tupla é semelhante a lista
print(meses[2])
'''


# Verificamos em qual indice um elemento está na tupla
'''
meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro')
print(meses.index('abril'))
# OBS: caso o elemento não exista, será retornado erro
'''


#  Slicing: tupla(inicio: fim: passo)
'''
meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro')
print(meses[0:])
'''

# Por que utilizar tuplas?

# - Tuplas são mais rápidas do que listas.
# - Tuplas deixam seu código mais seguro pois trabalhar com elementos imutáveis traz segurança


# Copiando uma tupla para outra (na tupla não há o problema de shallow copy)
'''
tupla = (1, 2, 3)
tupla2 = tupla
print(tupla, tupla2)
tupla = (1, 2, 99999)
print(tupla, tupla2)
'''
