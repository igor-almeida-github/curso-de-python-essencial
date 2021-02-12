"""
Listas

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem DINÂMICO
e também de podermos colocar QUALQUER tipo de dado.

Na linguagem C, possuem tamanho e tipo de dados fixo, ou seja, se você criar um array int com tamanho 5,
este array será sempre do tipo inteiro e poderá ter sempre no máximo 5 elementos. Já na linguagem python:

- Dinâmico: não possui tamanho fixo; ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo de dado;

As listas em python são representadas por colchetes: []

LISTAS SÂO MUTÁVEIS
"""
lista0 = [1, 3, 5, 11, 2, 44, 44, 13, 95]

lista1 = [1, 3, 4.3, -4, 'a']

lista2 = ['i', 'g', 'o', 'r', ' ', 'A', '.']

lista3 = []

lista4 = ['igor', 'almeida', 'goulart', 'ZZZ']

lista5 = list(range(11))

lista6 = list('igor almeida')


# Podemos facilmente checar se determinado valor está contido na lista
'''
if 8 in lista5:
    print('Econtrei o 8')
else:
    print('não encontrei o 8')
'''


# Podemos facilmente ordenar uma lista
'''
lista0.sort()
print(lista0)
'''
'''
lista2.sort()
print(lista2)
'''
'''
lista4.sort()
print(lista4)
'''


# Podemos facilmente contar o número de ocorrências de um valor em uma lista
'''
print(lista0.count(44))
'''


# Adicionar elementos em listas - para adicionar elementos em listas, utiliza-se a função append
# Com o append, nós só conseguimos adicionar 1 elemento por vez
'''
lista1.append(42)
print(lista1)
'''


# Com o extend é possivel adicionar mais de um elemento na lista de uma só vez, o argumento são iteraveis
'''
lista1.extend([1, 2, 3, 4])
print(lista1)
'''


# Podemos inserir um novo elemento na lista informando a posição do indice
# OBS: não substitui o valor original na posição indicada, o mesmo é deslocado para a direita
'''
lista1.insert(2, 'Novo Valor')
print(lista1)
'''


# Podemos juntar duas listas (concatenar)
'''
lista6 = lista1 + lista2
print(lista6)
'''


# Podemos inverter listas
'''
print(lista1)
lista1.reverse()
print(lista1)
'''
'''
print(lista1)
print(lista1[::-1])
'''


# Copiar uma lista
'''
lista6 = lista2.copy()
print(lista6)
'''


# Número de elementos em uma lista
'''
print(lista6)
print(len(lista6))
'''


# Podemos remover facilmente o último elemento de uma lista, lista1.pop() retorna o elemento removido
'''
print(lista1)
print(lista1.pop())
print(lista1)
'''


# Podemos remover um elemento pelo índice
# OBS: Os elementos á direita foram deslocados para a esquerda
'''
print(lista1)
print(lista1.pop(2))
print(lista1)
'''


# Podemos limpar a lista
'''
print(lista1)
lista1.clear()
print(lista1)
'''


# Podemos facilmente repetir elementos em uma lista
'''
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)
'''


# Podemos converter string em lista
'''
nome = 'igor almeida'
print(nome)
nome = nome.split()  # Lista com elementos separados pelo espaço
print(nome)
nome = 'igor almeida'
nome = list(nome)  # Lista com vários elementos, em que cada um elemento representa um caracter da string
print(nome)
'''


# O split permite escolher o separador
'''
nome = 'igor,alme ida,1,2,3'
print(nome)
nome = nome.split(',')  # O separador deixa de ser o espaço (padrão) e passa a ser a vírgula
print(nome)
'''


# Convertendo uma lista de volta em uma string
'''
nome = ['igor', 'Goulart', 'de', 'Almeida']
nome = ' '.join(nome)
print(nome)
'''


# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando tipos diferentes de dados
'''
lista7 = [1, True, 1.222, -200000, [1, 2], 'a', 'igor almeida', [], 88888999]
print(lista7)
# Iterando sobre listas
for elemento in lista7:
    print(elemento)
'''


# Utilizando variáveis em listas
'''
num1 = 1
num2 = 2
num3 = 3
numeros = [num1, num2, num3]
print(numeros)
'''


# Fazemos acesso aos elemento de forma indexada
'''
#           0         1         2        3
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])  # Verde
print(cores[3])  # Branco
# Fazer acesso aos elementos de forma indexada inversa
print(cores[-1])
print(cores[-4])
'''


# Gerar indices dos elementos
'''
cores = ['verde', 'amarelo', 'azul', 'branco']
for indice, cor in enumerate(cores):
    print(indice, cor)
'''


# Outros métodos não tão importantes mas também úteis
'''
# Encontrar o índice de um elemento na lista
numeros = [5, 6, 7, 8, 9, 9, 10]
# Em qual indice está o valor 6?
print(numeros.index(6))
# Em qual indice está o valor 6?
print(numeros.index(9))  # Dá o indice do primeiro 9 encontrado
# Em qual indice está o valor 23?
# print(numeros.index(23))  # Caso não tenha o elemento na lista, um erro ocorrerá
'''


# Podemos fazer busca dentro de um intervalo, ou seja, qual índice começar a buscar
'''
numeros = [9, 5, 9, 7, 8, 9, 10]
print(numeros.index(9, 1))  # Buscando a partir do índice 1
print(numeros.index(9, 3, 6))
'''


# Revisão de slicing
# lista = [inicio, fim, passo]
# range(inicio, fim, passo)
# Trabalhando com slice de lista com o parâmetro 'inicio'
'''
lista = [1, 2, 3, 4]
print(lista[1:])  # Iniciando no índice 1 e pegando todos os elementos restantes
print(lista[:2])  # Iniciando no índice 0 e pegando todos os elementos até o 2 (não inclusive)
print(lista[1:3])  # Iniciando no índice 1 e pegando todos os elementos até o 3 (não inclusive)
'''


# Trabalhando com slice de lista com o parâmetro 'passo'
'''
lista = [1, 2, 3, 4]
print(lista[::2])  # Começando no índice zero, vai até o final de 2 em 2
print(lista[-3::-1])  # O passo pode ser negativo e os limites também
print(lista[::-1])   # Inverte lista
'''


# Invertendo valores em uma lista
'''
nomes = ['igor', 'almeida']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)
nomes.reverse()
print(nomes)
'''


# Soma*, Valor máximo*, Valor mínimo*, Tamanho
# * Se os valores forem inteiros ou reais.
'''
lista = [1, 2, 3, 4, 5, 6]
print(sum(lista))  # Soma
print(max(lista))  # Valor máximo
print(min(lista))  # Valor mínimo
print(len(lista))  # Tamanho da lista
'''


# Transformar uma lista em tupla
'''
lista = [1, 2, 3, 4, 5, 6]
print(lista)
tupla = tuple(lista)
print(tupla)
'''


# Desempacotamento de lista
'''
lista = [1, 2, 3]
num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)
# OBS: se tivermos um número de elementos na lista diferente do números de variáveis para desempacotar, ocorrerá erro
'''


# Copiando uma lista para outra (Shallow copy, Deep copy)

# Forma 1, modificações na lista original não afetam a lista nova, pois elas são listas diferentes e independentes
# DEEP COPY : lista.copy()
lista = [1, 2, 3]
nova = lista.copy()
print(lista)
print(nova)
lista[1] = 999999
print(lista)
print(nova)

# Forma 2, modificar uma lista afeta a outra de modo que ocorre o mesmo com ambas ao modificar uma
# SHALLOW COPY
lista = [1, 2, 3]
nova = lista
print(lista)
print(nova)
lista[1] = 999999
print(lista)
print(nova)
