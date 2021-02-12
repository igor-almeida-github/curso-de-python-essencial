"""
Estruturas lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    - not
    - O is é a mesma coisa de == mas também serve para outras coisas, como por exemplo:
        nome = 'igor'

        print(nome.isprintable())

Operadores binários:
    - and, or, is

Exemplos unários:
    ativo = 1
    logado = not ativo
    print(logado)

Exemplos binários:
    ativo = True
    logado = True

    if ativo and logado:
        print('Bem vindo usuário')
    else:
        print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

    if ativo or logado:
        print('Bem vindo usuário')
    else:
        print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

    ativo = True
    logado = False
    if ativo is False:
        print('if retornou verdade')
    else:
        print('if retornou falso')

"""

nome = 'igor'

print(nome.isdecimal())

