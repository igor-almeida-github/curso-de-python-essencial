"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionário python são conhecidos por mapas.
Dicionários são coleções do tipo chave/valor.

com listas temos: (Chaves são implicitas)
chaves:   0, 1, 2
lista = [ 1, 2, 3]

Já dicionários as chaves são explicitas e tanto chave quanto valor podem ser qualquer tipo de dado, pode-se inclusive
misturar tipos diferentes
"""

# Dicionários são representados por chaves {}.
'''
print(type({}))
'''


# Exemplo de dicionário (chave e valor são separados por : ). Foma mais comum
'''
paises = {'br': 'brasil', 'us': 'united states', 'cn': 'china'}
print(paises)
print(paises['cn'])
'''


# Forma 2 de criação de dicionário (menos comum):
'''
paises = dict(br='brasil', us='united states', cn='china')
print(paises)
'''


# Acessando elementos
'''
paises = {'br': 'brasil', 'us': 'united states', 'cn': 'china'}
print(paises['br'])
print(paises['us'])
print(paises['cn'], '\n')
# OBS: Tentar acessar com uma chave que não existe retornará erro

# acessando via get
print(paises.get('br'))
print(paises.get('playstation'))
# OBS: Com o get, acessar com chave não existente não retona erro, ao invés disso retorna none
'''


# Condicional com o none, não dá erro
'''
paises = {'br': 'brasil', 'us': 'united states', 'cn': 'china'}
russia = paises.get('ru')
print(russia)
if russia:
    print('encontrei')
else:
    print('não encontrei')
'''


# Com o get também é possivel definir o retorno padrão em caso de não encontrar nada
'''
paises = {'br': 'brasil', 'us': 'united states', 'cn': 'china'}
russia = paises.get('playstation', 'Não encontrei')
print(russia)
'''


# Podemos determinar se uma chave se encontra presente no dicionário
'''
paises = {'br': 'brasil', 'us': 'united states', 'cn': 'china'}
print('br' in paises)  # True
print('ru' in paises)  # Falso
print('brasil' in paises)  # Falso
# Fazendo da maneira acima, ele não busca por valores, apenas por chaves
'''


# Evitando keyerror
'''
paises = {'br': 'brasil', 'us': 'united states', 'cn': 'china'}
if 'ru' in paises:
    russia = paises['ru']
else:
    russia = 'não encontrei'
print(russia)
'''


# Podemos utilizar qualquer tipo de dado no valor, mas o índice não aceita listas ou dicionários, outros tipos são
# aceitos
'''
dicio = {'oi': 'nada', 1: 'oque', 3.33: 33, 4: {'br': 'brasil', 'us': 'united states', 'cn': 'china'}, (1, 2): [1, 2]
         , None: 'nada', True: False}
print(dicio[True])
'''


# Adicionar elementos em um dicionário
'''
receita = {'Jan': 100, 'Fev': 120, 'Mar': 300}
print(receita)
# Forma 1 - Mais comum
receita['Abr'] = 22
print(receita)
# Forma 2
receita.update({'Mai': 500})
print(receita)
'''


# Atualizando dados em um dicionário
'''
# Forma 1
receita = {'Jan': 100, 'Fev': 120, 'Mar': 300}
print(receita)
receita['Jan'] = 555
print(receita)
# Forma 2
receita.update({'Mar': 1000})
print(receita)
# Conclusão 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma.
# Conclusão 2: Em dicionário não podemos ter chaves repetidas.
'''


# Remover dados de um dicionário
'''
# Forma 1 (mais comum)
receita = {'Jan': 100, 'Fev': 120, 'Mar': 300}
print(receita)
marco_lucro = receita.pop('Mar')
print(receita)
print(marco_lucro)
# OBS: Aqui precisamos sempre informar a chave e caso não encontre, um keyerror é retornado
# OBS: Ao removermos um objeto, o valor desse objeto é retornado

# Forma 2
del receita['Fev']
print(receita)
# OBS: Aqui precisamos sempre informar a chave e caso não encontre, um keyerror é retornado
# OBS: Ao removermos um objeto, o valor desse objeto NÃO é retornado
'''


#  Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras no qual adicionamos produtos.
'''
"""
Carrinho de compras:
    Produto 1:
        - nome:
        - quantidade:
        - preço:
    Produto 2:
        - nome:
        - quantidade:
        - preço:
"""
# 1 - Poderiamos usar uma lista para isso? SIM
carrinho = []
produto_1 = ['playstation 4', 1, 2300]
produto_2 = ['God of war', 1, 150]
carrinho.append(produto_1)
carrinho.append(produto_2)
print(carrinho)
# Teriamos que saber o índice de cada informação no produto.

# 2 - Poderiamos usar uma tupla para isso? SIM
produto_1 = ('playstation 4', 1, 2300)
produto_2 = ('God of war', 1, 150)
carrinho = (produto_1, produto_2)
print(carrinho)
# Teriamos que saber o índice de cada informação no produto.

# 3 - Poderiamos usar uma dicionário para isso? SIM
carrinho = []
produto_1 = {'nome': 'playstation 4', 'quantidade': 1, 'preço': 2300}
produto_2 = {'nome': 'God of War', 'quantidade': 1, 'preço': 150}
carrinho.append(produto_1)
carrinho.append(produto_2)
print(carrinho)
# Desta forma facilmente adicionamos e removemos produtos no carrinho e em cada produto podemos ter certeza sobre cada
# informação
'''


# Métodos de dicionários
'''
# Limpar o dicionário (zerar dados)
d = dict(a=1, b=2, c=3)
print(d)
d.clear()
print(d)
'''


# Copiando um dicionário para outro (Deep copy)
'''
d = dict(a=1, b=2, c=3)
print(d)
novo = d.copy()  # Deep copy
print(novo)
novo.update({'d': 4})
print(d)
print(novo)
'''


# Copiando um dicionário para outro (Shallow copy)
'''
d = dict(a=1, b=2, c=3)
print(d)
novo = d  # Shallow copy
print(novo)
novo.update({'d': 4})
print(d)
print(novo)
'''

'''
# Forma não usual de criação de dicionários
outro = {}.fromkeys('a', 'b')
print(outro)

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'],)
print(usuario)
# OBS: o método fromkeys recebe dois parâmetros: um iterável e um valor.
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.

veja = {}.fromkeys('igoooor', 'desconhecido')  # O 'o' não será repetido, pois em dicionário não há
# repetição de chave
print(veja)

veja = {}.fromkeys(range(5), 'desconhecido')
print(veja)
'''