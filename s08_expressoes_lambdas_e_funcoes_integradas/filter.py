"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.

"""
# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean

media = statistics.mean(dados)
# OBS: Assim como a função map(), a filter recebe dois parâmetros, sendo uma função
# e um iterável.

res = filter(lambda x: x > media, dados)

'''
print(f'{list(res)} - {list(res)}')  # Só printa uma vez, o objeto desaparece depois de ser utilizado, assim como na map
'''

'''
# Pode-se iterar sobre o objeto retornado pelo filter
for i in filter(lambda x: x > media, dados):
    print(i)
'''

'''
paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colômbia', '', 'Equador', '', '', 'Venezuela']
print(paises)
paises = list(filter(lambda x: x != '', paises))
print(paises)
'''

'''
paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colômbia', '', 'Equador', '', '', 'Venezuela']
print(paises)
paises = list(filter(None, paises))
print(paises)
'''

''' OBS:
Diferença entre map() e filter() é:
map() recebe dois parâmetros, uma função e um iterável e mapeia a função para cada elemento do iterável
filter() recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando apenas os elementos de acordo
a função 
'''

# Exemplo mais complexo. Filtrar os usuários que estão inativos no Twitter.
'''
usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

inativos = [nome['username'] for nome in list(filter(lambda x: not x['tweets'], usuarios))]
print(inativos)
'''

# Combinar filter() e map()
# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres
'''
nomes = ['Vanessa', 'Ana', 'Maria']

frases = list(map(lambda x: f'Sua instrutora é {x}', filter(lambda y: len(y) < 5, nomes)))
print(frases)
'''