"""
Escopo de variáveis

Dois casos de escopo:
1 - Variáveis globais:
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreende todo o programa.
2 - Variáveis locais:
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas ou seja, seu escopo
    está limitado ao bloco onde foi declarada.

Para declarar variáveis em python, fazemos:
nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que
ao declararmos uma variável nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuirmos o valor à mesma.

Exemplo em C:
int num = 42;

Exemplo em Java:
int num = 42;

Ao contrário do C, python permite reatribuição
num = 42 # Exemplo de variável global
print(num)
print(type(num))

num = 'oi'
print(num)
print(type(num))

"""

variavelglobal = 2  # Exemplo de variável global

if variavelglobal < 10:
    novo = variavelglobal+10
    print(novo)
# Essa variável é criada dentro do if, e só é criada se a condição do if for verdadeira,
# assim ela não faz parte do escopo global, para não dar o erro, o novo deve ser declarado fora do if
print(novo)

