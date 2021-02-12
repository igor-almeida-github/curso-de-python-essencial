"""
Módulo Collections - Default Dict
https://docs.python.org/3/library/collections.html#collections.defaultdict
- Para criar um default dict nós informamos um valor default, podendo utilizar um lambda para isso, este valor será
utilizado sempre que não houver um valor definido. Caso tentemos acessar uma chave que não existe, essa chave será
criada e o valor default será atribuído.

OBS: Lambdas são funções sem nome, que podem ou não receber parâmetros de entrada e retornar valores.
"""

# No dicionário ao tentarmos acessar uma chave que não exite, um erro é retornado
'''
dicionario = {'nome': 'igor goulart de almeida'}
print(dicionario)
print(dicionario['nome'])
# Veja o erro:
#print(dicionario['playstation'])
'''

# Já o Default Dict não apresenta keyerror
from collections import defaultdict

dicionario = defaultdict(lambda: 0)
print(dicionario)

dicionario['nome'] = 'igor'
print(dicionario)
print(dicionario['russia'])  # Se fosse um dicionário comum, daria keyerror
print(dicionario)  # Observa-se que foi criado o elemento com a chave informada e o valor padrão 0
