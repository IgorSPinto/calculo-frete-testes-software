from src.frete import calcular_frete


def test_calcular_frete_economico():
	assert calcular_frete(5, 100, "economica") == 25.00


def test_calcular_frete_padrao():
	assert calcular_frete(5, 100, "padrao") == 30.00


def test_calcular_frete_expressa():
	assert calcular_frete(5, 100, "expressa") == 37.50