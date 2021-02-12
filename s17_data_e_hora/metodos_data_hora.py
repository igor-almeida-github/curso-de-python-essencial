"""
Métodos de Data e Hora


"""
import datetime
#from textblob import TextBlob
import timeit
import functools

# Com now() podemos especificar um fuso horário (timezone)
'''
agora = datetime.datetime.now()
print(agora)
print(type(agora))
print(repr(agora))

print('-------------------------')

hoje = datetime.datetime.today()
print(hoje)
print(type(hoje))
print(repr(hoje))

'''

# Mudanças ocorrendo à meia-noite - combine()
'''
manutencao = datetime.datetime.combine(datetime.datetime.now() + datetime.timedelta(days=1), datetime.time())

print(manutencao)
print(type(manutencao))
print(repr(manutencao))
'''

# Encontrar o dia da semana. weekday()
'''
# 0 - Segunda
# 1 - Terça-feira
# 2 - Quarta-feira
# 3 - Quinta-feira
# 4 - Sexta feira
# 5 - Sábado
# 6 - Domingo

manutencao = datetime.datetime.combine(datetime.datetime.now() + datetime.timedelta(days=1), datetime.time())

print(manutencao.weekday())
'''
'''
nascimento = input('Informe sua data de nascimento (dd/mm/yy): ')

nascimento = nascimento.split('/')

nascimento = reversed(nascimento)

nascimento = list(map(int, nascimento))

nascimento = datetime.datetime(*nascimento)

dia_da_semana = ['segunda', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta feira', 'sábado', 'domingo']

print(f'Você nasceu em um(a) {dia_da_semana[nascimento.weekday()]}.')
'''

# Formatando datas/horas com strftime() (String Format Time)
'''
hoje = datetime.datetime.today()
print(hoje)
hoje_formatado = hoje.strftime('%d/%m/%Y')
print(hoje_formatado)
hoje_formatado = hoje.strftime('%d/%m/%y')
print(hoje_formatado)
hoje_formatado = hoje.strftime('%d/%B/%y')
print(hoje_formatado)
# OBS: outras formatações podem ser encontradas na tabela da documentação.
'''
'''

def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"


print(formata_data(datetime.datetime.now()))
print(TextBlob('Have you ever seen the rain?').translate(to='pt-br'))
'''
'''
nascimento = datetime.datetime.strptime('10/04/1998', '%d/%m/%Y')
print(nascimento)
'''
# Somente a hora
'''
almoco = datetime.time(12, 30, 0)
print(almoco)
'''

# Marcando o tempo de execução com timeit
'''
# Loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tempo)

# List Comprehension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(tempo)

# Map
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(tempo)
'''

'''
def teste(n):
    soma = 0
    for num in range(200 * n):
        soma = soma + num * 4
    return soma


print(timeit.timeit(functools.partial(teste, 2), number=10000))
'''
