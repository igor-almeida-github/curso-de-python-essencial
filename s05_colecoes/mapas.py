"""
Mapas - Conhecidos em python como dicionários

Dicionários em python são representandos por chaves {}
"""

# Iterar sobre dicionários
'''
receita = {'Jan': 100, 'Fev': 120, 'Mar': 300}
print(receita)
for key in receita:
    print(key, receita[key])
'''


# Acessando todas as chaves
'''
receita = {'Jan': 100, 'Fev': 120, 'Mar': 300}
print(receita.keys())
for chave in receita.keys():
    print(chave)
'''


# Acessando os valores
'''
receita = {'Jan': 100, 'Fev': 120, 'Mar': 300}
print(receita.values())
for valor in receita.values():
    print(valor)
'''


# desempacotamento de dicionários
'''
receita = {'Jan': 100, 'Fev': 120, 'Mar': 300}
print(receita.items())
for chave, valor in receita.items():
    print(chave, valor)
'''


# Soma*, Valor máximo*, Valor mínimo*, Tamanho
# OBS: se os valores forem inteiros/reais
receita = {'Jan': 100, 'Fev': 120, 'Mar': 300}
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
