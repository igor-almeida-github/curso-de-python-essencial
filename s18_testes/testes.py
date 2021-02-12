import unittest
from atividades import comer, dormir, e_engracada

'''
class AtividadesTestes(unittest.TestCase):

    def test_comer(self):
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma.'
        )

        self.assertEqual(
            comer(comida='pizza', e_saudavel=False),
            'Estou comendo pizza porque a gente só vive uma vez'
        )

# Ran 1 test in 0.001s
'''


# Refatorando para rodar os dois testes:
class AtividadesTestes(unittest.TestCase):

    def test_comer_saudavel(self):
        """Testando o retorno com comida saudável"""
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma.'
        )

    def test_comer_nao_saudavel(self):
        """Testando o retorno com comida não saudável"""
        self.assertEqual(
            comer(comida='pizza', e_saudavel=False),
            'Estou comendo pizza porque a gente só vive uma vez'
        )

    def test_dormir_pouco(self):
        """Testando o retorno dormindo pouco"""
        self.assertEqual(
            dormir(4),
            'Continuo consado após dormir por 4 horas. :('
        )

    def test_dormir_muito(self):
        """Testando o retorno dormindo muito"""
        self.assertEqual(
            dormir(10),
            'Dormi muito! Estou atrasado para o trabalho. '
        )

    def test_e_engracada(self):
        # self.assertEqual(e_engracada('Sérgio Malandro'), False)  # O None não é reconhecido com false
        self.assertFalse(e_engracada('Sérgio Malandro'))  # O None é reconhecido com false
        self.assertTrue(e_engracada('Jim Carrey'), 'Jim Carrey deveria ser engraçado')


if __name__ == '__main__':
    unittest.main()




