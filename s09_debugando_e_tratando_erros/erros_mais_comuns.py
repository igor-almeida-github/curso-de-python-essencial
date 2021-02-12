"""
Erros mais comuns em Python

É importante prestar atenção e aprender a ler as saídas de erros geradas pela execução do nosso código.

Os erros mais comuns:

SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, você escreveu algo que o Python não
reconhece como parte da linguagem.
# Exemplos SyntaxError:
# a)
def funcao:
    print('igor')
# b)
None = 1
def = 1
# c)
return

NameError -> Ocorre quando uma variável ou função não foi definida.
# Exemplos NameError:
# a)
print(geek)
# b)
geek()
# c)
a = 18
if a < 10:
    msg = 'é menor que 10'
print(msg)

TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado.
# Exemplos TypeError:
# a)
print(len(5))
# b)
print('Geek' + [])

IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando um
índice inválido.
# Exemplos IndexError:
# a)
lista = ['Geek']
print(lista[2])
# b)
tupla = ('Geek',)
print(tupla[2])

ValueError -> Ocorre quando uma função/operação built-in (integrada) recebe um argumento com o tipo correto, mas
com valor inapropriado.
# Exemplos ValueError:
# a)
print(int('a'))

KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe.
# Exemplos KeyError:
# a)
dic = {}
print(dic['geek'])

AttributeError -> Ocorre quando uma variável não tem um atributo/função.
# Exemplos AttributeError:
# a)
tupla = 11, 2, 31, 4
tupla.sort()
print(tupla)

IdentantionError -> Ocorre quando não respeitamos a identação do Python (4 espaços)
# Exemplos IdentantionError:
# a)
def nova():
print('Igor')

OBS: Exceptions e Erros são sinônimos na programação.
"""






