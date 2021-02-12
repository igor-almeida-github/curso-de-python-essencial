"""
Manipulando Data e Hora

Python tem um módulo built-in (integrado) para se trabalhar com data e hora
chamado datetime

"""
import datetime

# print(dir(datetime))

# print(datetime.MAXYEAR)

# print(datetime.MINYEAR)

print(datetime.datetime.now())  # 2020-05-15 18:32:10.592735

# print(repr(datetime.datetime.now()))  # datetime.datetime(year, month, day, hour, minute, second, microsecond)

# replace() para fazer ajustes na data/hora
'''
inicio = datetime.datetime.now()

print(inicio)

# Alterar o horário para 16 horas, 0 minutos, 0 segundos, 0 microsegundos
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)
print(inicio)
'''
'''
evento = datetime.datetime(2019, 1, 31, 0)

print(type(evento))

print(evento)

data = str(evento)

data = data[8:10] + '/' + data[5:7] + '/' + data[0:4]

print(data)
'''
'''
nascimento = input('Informe sua data de nascimento (dd/mm/yy): ')

nascimento = nascimento.split('/')

nascimento = reversed(nascimento)

nascimento = list(map(int, nascimento))

nascimento = datetime.datetime(*nascimento)

print(nascimento)
'''

# Acesso individual dos elementos da data e hora

# evento = datetime.datetime.now()
'''
print(evento.day)
print(evento.month)
print(evento.year)

print(evento.hour)
print(evento.minute)
print(evento.second)
print(evento.microsecond)
'''

# print(dir(evento))


