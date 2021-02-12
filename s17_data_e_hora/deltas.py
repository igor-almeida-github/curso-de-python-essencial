"""
Trabalhando com deltas de data e hora

delta = data_final - data_inicial


"""

import datetime

'''
data_hoje = datetime.datetime.now()

aniversario = datetime.datetime(2021, 3, 2)

tempo_para_evento = aniversario - data_hoje

print(type(tempo_para_evento))
print(tempo_para_evento)
print(repr(tempo_para_evento))

print(f'Faltam {tempo_para_evento.days} dias, {tempo_para_evento.seconds // 60 // 60} horas e '
      f'{tempo_para_evento.seconds // 60} min')

# Dica:
# print(24610 / 77)  # Float
# print(24610 // 77)  # Divisão inteira
'''

# data_hoje = datetime.datetime.now()
#
# tempo_a_partir_de_hoje = datetime.timedelta(days=22000)
#
# data_futura = data_hoje + tempo_a_partir_de_hoje
#
# print(data_futura)

producao = datetime.datetime(2020, 7, 1, 15, 54, 0)
data_hoje = datetime.datetime.now()
delta = data_hoje - producao
print(delta.days)
