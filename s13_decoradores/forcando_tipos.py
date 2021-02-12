"""
Forçando tipos de dados com decoradores.


"""


def forca_tipo(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):
            nova_args = []
            for (valor, tipo) in zip(args, tipos):
                nova_args.append(tipo(valor))
            return funcao(*nova_args, **kwargs)
        return converte
    return decorador


@forca_tipo(str, int)
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)


repete_msg('wow', 3)
repete_msg('Igor', '3')
repete_msg(45, '3')


