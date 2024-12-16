import unittest
from conversao import metros_para_milhas, milhas_para_metros

class TestConversao(unittest.TestCase):

    def test_metros_para_milhas(self):
        # Usando assertAlmostEqual para considerar uma pequena margem de erro
        self.assertAlmostEqual(metros_para_milhas(1609.34), 1, places=2)

    def test_milhas_para_metros(self):
        # Usando assertAlmostEqual para considerar uma pequena margem de erro
        self.assertAlmostEqual(milhas_para_metros(1), 1609.34, places=2)

if __name__ == '__main__':
    unittest.main()
