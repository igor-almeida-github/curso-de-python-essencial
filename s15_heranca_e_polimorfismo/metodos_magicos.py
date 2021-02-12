"""
POO - Métodos Mágicos

Métodos Mágicos são todos os métodos que utilizam dunder.

dunder init -> __init__()

__repr__ -> Representação do objeto


Representação Padrão:
<__main__.Livro object at 0x031814B0>
<__main__.Livro object at 0x03181970>


"""


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas

    def __repr__(self):  # Faz a representação do objeto (estamos sobrescrevendo)
        return f'{self.__titulo} escrito por {self.__autor}'

    def __str__(self):  # Executa __str__ e se não tiver __str__ então executa o __repr__
        return self.__titulo

    def __len__(self):
        return self.__paginas

    def __del__(self):
        print('Um objeto do tipo Livro foi deletado')

    def __add__(self, outro):
        return f'{self} - {outro}'

    def __mul__(self, other):
        if isinstance(other, int):
            return (self.__titulo + ' ') * other
        else:
            raise TypeError('Não posso multiplicar')


livro1 = Livro('Python Rocks!', 'Geek University', 400)
livro2 = Livro('IA', 'Geek University', 420)

print(livro1)

print(repr(livro1))

print(len(livro1))

# del livro1

print(livro1 + livro2)

print(livro1 * 3)

