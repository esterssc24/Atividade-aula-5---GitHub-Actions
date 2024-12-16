import unittest
from conversao import metros_para_km, metros_para_milhas, km_para_metros, milhas_para_metros

class TestConversao(unittest.TestCase):
    
    def test_metros_para_km(self):
        self.assertEqual(metros_para_km(1000), 1)
        self.assertEqual(metros_para_km(500), 0.5)

    def test_metros_para_milhas(self):
        self.assertEqual(metros_para_milhas(1609.34), 1)
        self.assertEqual(metros_para_milhas(804.67), 0.5)

    def test_km_para_metros(self):
        self.assertEqual(km_para_metros(1), 1000)
        self.assertEqual(km_para_metros(0.5), 500)

    def test_milhas_para_metros(self):
        self.assertEqual(milhas_para_metros(1), 1609.34)
        self.assertEqual(milhas_para_metros(0.5), 804.67)

if __name__ == '__main__':
    unittest.main()
