<<<<<<< HEAD
import pytest
from conversions import metros_para_km, metros_para_milhas, km_para_metros, milhas_para_metros

def test_metros_para_km():
    assert metros_para_km(1000) == 1
    assert metros_para_km(0) == 0

def test_metros_para_milhas():
    assert pytest.approx(metros_para_milhas(1609.34), 0.001) == 1  # tolerância para floats

def test_km_para_metros():
    assert km_para_metros(1) == 1000
    assert km_para_metros(0) == 0

def test_milhas_para_metros():
    assert pytest.approx(milhas_para_metros(1), 0.001) == 1609.34
=======
import unittest
from conversao import metros_para_km, metros_para_milhas, km_para_metros, milhas_para_metros

class TestConversao(unittest.TestCase):
    def test_metros_para_km(self):
        self.assertEqual(metros_para_km(1000), 1)
        self.assertEqual(metros_para_km(500), 0.5)
        self.assertEqual(metros_para_km(1500), 1.5)
    
    def test_metros_para_milhas(self):
        self.assertEqual(metros_para_milhas(1609.34), 1)
        self.assertEqual(metros_para_milhas(1000), 0.621371)
        self.assertEqual(metros_para_milhas(500), 0.310685)
    
    def test_km_para_metros(self):
        self.assertEqual(km_para_metros(1), 1000)
        self.assertEqual(km_para_metros(0.5), 500)
        self.assertEqual(km_para_metros(2), 2000)
    
    def test_milhas_para_metros(self):
        self.assertEqual(milhas_para_metros(1), 1609.34)
        self.assertEqual(milhas_para_metros(0.5), 804.67)
        self.assertEqual(milhas_para_metros(2), 3218.68)

if __name__ == '__main__':
    unittest.main()
>>>>>>> f63b9701f39e9f38162065bffac73abf45cada0a
