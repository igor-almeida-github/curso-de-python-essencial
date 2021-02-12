"""
Escrevendo um iterador customizado


"""


class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration


'''
con = Contador(1, 4)
print(next(con))
print(next(con))
print(next(con))
# print(next(it))  # StopIteration Error
'''
'''
for n in Contador(1, 20):
    print(n)
'''
