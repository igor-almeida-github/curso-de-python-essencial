def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f'{texto.title()}\n{"-" * len(texto)}'

    else:
        return f'{texto.title()}'.center(50, '#')


print(cabecalho('geek university'))
print(cabecalho('geek university', False))
print(cabecalho('geek university', 'Igor'))

# Escrever no terminal: mypy arquivo_mypy.py






