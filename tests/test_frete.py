import pytest

from src.frete import calcular_frete


@pytest.mark.parametrize(
	"tipo_entrega, resultado_esperado",
	[
		("economica", 25.00),
		("padrao", 30.00),
		("expressa", 37.50),
	],
	ids=["economica", "padrao", "expressa"],
)
def test_calcular_frete_por_tipo_entrega(tipo_entrega, resultado_esperado):
	assert calcular_frete(5, 100, tipo_entrega) == resultado_esperado


@pytest.mark.parametrize("peso", [0.1, 30], ids=["minimo", "maximo"])
def test_calcular_frete_aceita_limites_validos_de_peso(peso):
	calcular_frete(peso, 100, "economica")


@pytest.mark.parametrize(
	"peso",
	[0, 0.09, 30.01, 31],
	ids=["zero", "abaixo-minimo", "pouco-acima-maximo", "muito-acima-maximo"],
)
def test_calcular_frete_rejeita_peso_invalido(peso):
	with pytest.raises(ValueError):
		calcular_frete(peso, 100, "economica")


@pytest.mark.parametrize("distancia", [1, 1000], ids=["minima", "maxima"])
def test_calcular_frete_aceita_limites_validos_de_distancia(distancia):
	calcular_frete(5, distancia, "economica")


@pytest.mark.parametrize(
	"distancia",
	[0, 1001],
	ids=["abaixo-minimo", "acima-maximo"],
)
def test_calcular_frete_rejeita_distancia_invalida(distancia):
	with pytest.raises(ValueError):
		calcular_frete(5, distancia, "economica")


def test_calcular_frete_rejeita_tipo_entrega_invalido():
	with pytest.raises(ValueError):
		calcular_frete(5, 100, "urgente")