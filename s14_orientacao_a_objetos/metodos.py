"""
POO - Métodos

- Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode
realizar no seu sistema.

Em Python, dividimos os métodos, em 2 grupo: Métodos de instância e Métodos de Classe.

Métodos de Instância:

# O método dunder init __init__ é um método especial chamada de construtor e sua função é construir o
objeto a partir da classe

OBS: Os métodos/funções dunder em Python são chamados de métodos mágicos.

# Métodos são escritos em letras minúsculas. Se o nome for composto, o nome terá as palavras separadas por _

# Métodos de Classe em Python são conhecidos como Métodos Estáticos em outras linguagens
"""

from passlib.hash import pbkdf2_sha256 as cryp


# Métodos de Instância
'''
class Lampada:

    def __init__(self, cor, tensao, luminosidade):
        self.__cor = cor
        self.__tensao = tensao
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        ContaCorrente.contador = self.__numero
        self.__limite = limite
        self.__saldo = saldo


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        Produto.contador = self.__id
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor

    def desconto(self, porcentagem):
        """Retorna o valor do produto com desconto"""
        return self.__valor * (1 - porcentagem / 100)


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)

    # Não é recomendado que criemos métodos próprios com dunder, pois isso é para metodos mágicos.
    # def __correr__(self, metros):
    #     print(f'{self.__nome} está correndo {metros} metros')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False
'''

'''
p1 = Produto('Playstation', 'Video Game', 2400)
print(p1.desconto(20))
print(Produto.desconto(p1, 20))  # self, desconto

u1 = Usuario('igor', 'almeida', 'igoralmeida@gmail.com', '1234')
print(Usuario.nome_completo(u1))
print(u1.nome_completo())
'''
'''
nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o e-mail: ')
senha = input('Informe a senha: ')
confirma_senha = input('Confirme a senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
    print('Usuário criado com sucesso')

else:
    print('Senha não confere...')
    exit(1)

senha = input('Informe a senha para acesso: ')
if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado')

print(f'Senha criptografada: {user._Usuario__senha}')  # Acesso não recomendado
'''


# Métodos de Classe - Não estão vinculados a nenhuma instância de classe e sim diretamente a classe.
'''
class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Temos {cls.contador} usuários no sistema')

    @classmethod
    def ver(cls):
        print('Teste')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        Usuario.contador = self.__id
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)


user = Usuario('igor', 'almeida', 'igor@gmail.com', '12345')
Usuario.conta_usuarios()  # Forma correta, pois trata-se de um método de classe.
user.conta_usuarios()  # Possível, mas não recomendada.
'''


# Podemos criar métodos privados
class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Temos {cls.contador} usuários no sistema')

    @classmethod
    def ver(cls):
        print('Teste')

    @staticmethod
    def definicao():
        return 'UXR344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        Usuario.contador = self.__id
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        print(f'Usuário criado: {self.__gera_usuario()}')

    def __gera_usuario(self):
        return self.__email.split('@')[0]


user = Usuario('igor', 'almeida', 'igor12@gmail.com', '123456')
# print(user.__gera_usuario())  # AttributeError
# print(user._Usuario__gera_usuario())  # Acesso externo de método privado não recomendado
print(Usuario.definicao())

