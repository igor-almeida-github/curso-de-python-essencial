"""
Geradores

- Geradores (Generators) são Iterators (Iteradores);
OBS: O contrário não é verdadeiro. Ou seja, nem todo iterator é um generator.

Outras informações:
- Generators podem ser crados com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com Expressões Geradoras;

Diferenças entre Funções e Generator Functions (Funções Geradoras)

---------------------------------------------------------------------------------
| Funções                               | Generator Functions                   |
---------------------------------------------------------------------------------
| utilizam return                       | utilizam yield                        |
---------------------------------------------------------------------------------
| retorna uma vez                       | pode utilizar yield mútiplas vezes    |
---------------------------------------------------------------------------------
| quando executada, retorna um valor    | quando executada, retorna um generator|
---------------------------------------------------------------------------------

"""


# Exemplo Generator Function
def conta_at(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1
# OBS: Uma Generator Function não é um Generator. Ela gera um generator.


'''
for i in conta_at(10):
    print(i)
'''
'''
ger = conta_at(3)
print(type(ger))
print(ger)
print(next(ger))
print(next(ger))
print(next(ger))
# print(next(ger))  # StopIteration Error
'''
'''
ger = conta_at(3)
print(next(ger))  # 1
print('-------')
for i in ger:  # Vai começar do 2, pois o 1 já foi retornado no primeiro next
    print(i)
'''
'''
print(list(conta_at(10)))
'''



