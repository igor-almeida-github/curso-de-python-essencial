# def cumprimentar(nome: str) -> str:
#     return f'Olá, {nome}'
#
#
# print(cumprimentar('igor'))


def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f'{texto.title()}\n{"-" * len(texto)}'
    else:
        return f'{texto.title()}'.center(50, '#')


print(cabecalho('geek university'))
print(cabecalho('geek university', False))
# print(cabecalho('geek university', 'Igor'))
# O python não impede de executar, mas a IDE marca e existem ferramentas de checagem de tipos.
