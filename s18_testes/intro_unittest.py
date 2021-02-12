"""
Introdução ao módulo Unittest

https://docs.python.org/3/library/unittest.html

Unittest -> Testes Unitários

O que são testes unitários?

Teste é a forma de se testar unidades individuais de código fonte.

Unidades individuais podem ser: funções, métodos, classes, módulos, etc.

# OBS: Teste unitário não é específico da linguagem Python.

Para criar nossos testes, criamos classes que herdam de unittest.TestCase
e a partir de então ganhamos todos os 'assertion' presentes no módulo.

Para rodar os testes, utilizamos unittest.main()

TesteCase -> Bagagem de testes para sua unidade.

# Conhecendo as assertions
-------------------------------------------------
Método:                     Checa se:
-------------------------------------------------
assertEqual(a, b)           a == b
assertNotEqual(a, b)        a != b
assertTrue(x)               bool(x) is True
assertFalse(x)              bool(x) is False
assertIs(a, b)              a is b
assertIsNot(a, b)           a is not b
assertIsNone(x)             x is None
assertIsNotNone(x)          x is not None
assertIn(a, b)              a in b
assertNotIn(a, b)           a not in b
assertIsInstance(a, b)      isinstance(a, b)
assertNotIsInstance(a, b)   not isinstance(a, b)

Por convenção, todos os testes em um test case devem ter seu nome iniciado com test_

# Para executar os testes com unittest

python nome_do_modulo.py

# Para executar os testes com unittest no modo verbose (detalhes)

python nome_do_modulo -v

Podemos acrescentar (e é recomendado) docstrings nos nossos testes.



-------------------------------------------------

"""
import unittest

# Prática - Utilizando a abordagem TDD




