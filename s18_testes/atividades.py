def comer(comida, e_saudavel):
    if e_saudavel:
        return f'Estou comendo {comida} porque quero manter a forma.'
    else:
        return f'Estou comendo {comida} porque a gente só vive uma vez'


def dormir(num_horas):
    if num_horas < 8:
        return f'Continuo consado após dormir por {num_horas} horas. :('
    else:
        return f'Dormi muito! Estou atrasado para o trabalho. '


def e_engracada(pessoa):
    if pessoa == 'Sérgio Malandro':
        return False
    else:
        return True
