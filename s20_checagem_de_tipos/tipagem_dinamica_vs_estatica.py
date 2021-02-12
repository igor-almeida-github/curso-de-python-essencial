"""
Tipagem de dados Dinâmica vs Estática
"""

# Tipagem dinâmica:

'''
idade = 42

print(type(idade))

idade = 'Quarenta e dois'

print(type(idade))
'''

# Problema com a tipagem dinâmica: (Problema pode aparecer somente durante a execução)
'''
if False:
    resultado = 1 + 'Geek'
else:
    resultado = 1 + 41

print(resultado)
'''


