"""
Levantando os próprios erros com o raise

raise -> Lança exceções

OBS: O raise não é uma função. É uma palavra  reservada, assim como def ou qualquer outra em Python.
Para simplificar, pense no raise como sendo útil para criar nossas próprias exceções e mensagens de erro.

A forma geral de utilização é:
raise TipoDoErro('Mensagem de erro')

OBS: O raise, assim como o return, finaliza a função. Ou seja, nada após o raise é executado.
"""


# Exemplo 1
'''
def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f"O texto '{texto}' será impresso na cor {cor}.")


colore('Igor', [1, 2])
'''
# Exemplo 2
'''
def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError('cor precisa ser verde, amarelo, azul ou branco')
    print(f"O texto '{texto}' será impresso na cor {cor}.")


colore('Igor', 'verde')
'''




