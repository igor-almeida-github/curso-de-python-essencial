"""
Tipo none
O tipo de dado None em python representa o tipo sem tipo, ou poderia ser conhecido também
como tipo vazio, porém falar que é um tipo sem tipo é mais apropriado.

OBS: o tipo None é sempre especificado com a primeira letra maiúscula.

Quando utilizar?
- Podemos utilizar None quando queremos criar uma variável e inicializá-la com um tipo sem tipo, antes de recebermos
um valor final
"""

num = None
print(num)
print(type(num))

# O tipo none sempre será falso
if None:
    print('verdade')
else:
    print('falso')
