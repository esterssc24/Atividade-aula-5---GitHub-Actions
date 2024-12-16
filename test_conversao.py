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
