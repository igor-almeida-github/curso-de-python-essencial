"""
Definindo Funções

- Funções são pequenas partes de código que realizam tarefas específicas;
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito úteis para executar procedimentos similares por repetidas vezes;
# DRY - Don't Repeat Yourself

# Como definir funções?
# Em Python, a forma geral de definir funções é:

def nome_da_funcao(parametros_de_entrada):
    bloco da função

Onde:
- nome_da_funcao sempre com letras minúsculas e se for nome composto, separado por underline.
- parametros_de_entrada são opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais
ou não.
- Bloco da função, também chamado de corpo da função ou implementação, é onde o processamento acontece, neste bloco
pode ter ou não retorno da função.
- Para definir uma função utilizamos a palavra reservada def, informando ao Python que estamos definindo uma função,
também abrimos o bloco de código com o já conhecido ':' que é utilizado em Python para definir blocos.

OBS: Se você escrever uma função que realiza várias tarefas dentro dela, é bom fazer uma verificação para que
a função seja simplificada.

Já utilizamos várias funções desde o início do curso:
- ex: print(), len(), max(), count(), etc ...
"""

# Exemplo de utilização de funções:
'''
cores = ['verde', 'vermelho', 'amarelo', 'branco']

# Utilizando a funções integradas (Built-in) do Python print() e append() e clear()
print(cores)
cores.append('roxo')  # A função append aqui é atribuída a lista
print(cores)
cores.clear()
print(cores)
'''


# Definindo função

def diz_oi():
    print('oi!')


def cantar_parabens():
    print('Parabéns para você')
    print('nessa data querida')
    print('muitas felicidades')
    print('muitos anos de vida')


"""
OBS: 
1 - Veja que dentro das nossas funções, podemos utilizar outras funções;
2 - Veja que nossa função só executa uma tarefa, ou seja, ela só diz oi;
3 - Veja que esta função não recebe nenhum parâmetro de entrada;
4 - Veja que esta função não retorna nada;
"""

# Utilizando função:
'''
diz_oi()  # Chamada de execução

cantar_parabens()
cantar_parabens()
cantar_parabens()
'''


# Em Python, podemos inclusive criar variáveis do tipo de uma função e executar esta função através da variável
'''
canta = cantar_parabens
canta()
'''
