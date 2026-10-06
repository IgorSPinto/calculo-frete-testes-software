import pytest

from src.frete import calcular_frete


def test_calcular_frete_economico():
	assert calcular_frete(5, 100, "economica") == 25.00


def test_calcular_frete_padrao():
	assert calcular_frete(5, 100, "padrao") == 30.00


def test_calcular_frete_expressa():
	assert calcular_frete(5, 100, "expressa") == 37.50


def test_calcular_frete_peso_abaixo_minimo():
	with pytest.raises(ValueError):
		calcular_frete(0.09, 100, "economica")


def test_calcular_frete_peso_acima_maximo():
	with pytest.raises(ValueError):
		calcular_frete(30.01, 100, "economica")


def test_calcular_frete_distancia_abaixo_minimo():
	with pytest.raises(ValueError):
		calcular_frete(5, 0, "economica")


def test_calcular_frete_distancia_acima_maximo():
	with pytest.raises(ValueError):
		calcular_frete(5, 1001, "economica")


def test_calcular_frete_tipo_entrega_invalido():
	with pytest.raises(ValueError):
		calcular_frete(5, 100, "urgente")