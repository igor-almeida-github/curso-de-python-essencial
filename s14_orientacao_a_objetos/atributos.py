"""
POO - Atributos
Atributos -> Representam as características do objeto. Ou seja, pelos atributos nós
conseguimos representar computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de instâncias;
    - Atributos de classe;
    - Atributos Dinâmicos;

# Atributos de instância: São atributos declarados dentro do método construtor.
# OBS: Método construtor: É um método especial utilizado para a construção do objeto.
# Os atributos de instância terão seu valor definido a cada instância criada.

Em Python, por convenção, ficou estabelecido que todo atributo de uma classe é público.
Ou seja, pode ser acessado em todo o projeto.
Caso queiramos demonstrar que determinado atributo deve ser tratado como privado, ou seja,
que deve ser acessado/utilizado somente dentro da própria classe onde está declarado,
utiliza-se __ duplo underscore no início de seu nome.

Isso é conhecido também como Name Mangling.

# Atributos de classe: são atributos que são declarados diretamente na classe, ou seja, fora do construtor. Geralmente
# já inicializamos um valor e este valor é compartilhado entre todas as instâncias da classe. Ou seja, ao
# invés de cada instância ter seus próprios valores como é o caso dos atributos de instâncias, com os
# atributos de classe todas as instâncias terão seu valor para este atributo

# Atributos Dinâmicos: Um atributo de instância que pode ser criado em tempo de execução. O atributo dinâmico
# será exclusivo da instância que o criou.

"""


# Classes com atributos de instância públicos
'''
class Lampada:

    def __init__(self, tensao, cor):
        self.tensao = tensao
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

'''
'''
class Teste:
    
    def __init__(cerveja, nome, idade):  # É possível usar outro nome ao invês de self, mas não é recomendado.
        cerveja.nome = nome
        cerveja.idade = idade
'''


# # Classes com atributos de instância privados
'''
class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)

'''
# OBS: Lembre-se que isso é apenas um convenção, ou seja, a linguagem Python não vai
# impedir que façamos acesso aos atributos sinalizados como privados fora da classe.
# Exemplo:
'''
user = Acesso('user@gmail.com', '12345')

print(user.email)
# print(user.__senha)  # AttributeError
print(dir(user))
print(user._Acesso__senha)  # Temos acesso. Mas não deveríamos fazer este acesso. (Name Mangling)
'''
'''
user = Acesso('user@gmail.com', '12345')
user.mostra_senha()
user.mostra_email()
'''

# O que significa atributos de instância?
# Significa que ao criarmos instâncias/objetos de uma classe, todas as instâncias terão valores próprios
# para estes atributos.
'''
user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '543210')

user1.mostra_email()
user2.mostra_email()
'''


# Atributos de Classe:
'''
class Produto:

    # Atributo de classe
    imposto = 1.05  # 5% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor * Produto.imposto
        Produto.contador = self.id


p1 = Produto('Playstation 4', 'Video Game', 2300)
print(p1.imposto)  # Acesso possível, mas incorreto de um atributo de classe
print(p1.valor)  

# OBS: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe:
print(Produto.imposto)  # Acesso correto de um atributo de classe
p2 = Produto('Xbox', 'Video Game', 555)

print(p1.id)
print(p2.id)

# OBS: Em linguagens como Java, os atributos conhecidos como atributos de classe aqui em Python, são chamados de
# atributos estáticos:
'''


# Atributos Dinâmicos:
'''
class Produto:

    atributo_de_classe = 1

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


p1 = Produto('Arroz', 'Mercado', 5.23)
# Criando um atributo dinâmico em tempo de execução
p1.peso = '5kg'  # Note que na classe Produto não existe o atributo peso
print(p1.peso)
p2 = Produto('Feijão', 'Mercado', 5.23)
# print(p2.peso)  # AttributeError: 'Produto' object has no attribute 'peso'
print(p1.__dict__)
print(p2.__dict__)
# print(Produto.__dict__)
# Deletando atributos - É possível deletar tanto atributos dinâmicos quanto atributos de instância de um objeto
del p1.peso
del p2.nome
print(p1.__dict__)
print(p2.__dict__)
'''
