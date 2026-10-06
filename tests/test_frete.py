from src.frete import calcular_frete


def test_calcular_frete_economico():
	assert calcular_frete(5, 100, "economica") == 25.00