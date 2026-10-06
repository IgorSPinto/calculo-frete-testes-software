TAXA_BASE = 10
VALOR_POR_KG = 2
VALOR_POR_KM = 0.05
PESO_MINIMO = 0.1
PESO_MAXIMO = 30
DISTANCIA_MINIMA = 1
DISTANCIA_MAXIMA = 1000
MULTIPLICADORES_ENTREGA = {
	"economica": 1.00,
	"padrao": 1.20,
	"expressa": 1.50,
}


def _validar_entrada(peso, distancia, tipo_entrega):
	if not PESO_MINIMO <= peso <= PESO_MAXIMO:
		raise ValueError("Peso deve estar entre 0.1 e 30 kg")
	if not DISTANCIA_MINIMA <= distancia <= DISTANCIA_MAXIMA:
		raise ValueError("Distancia deve estar entre 1 e 1000 km")
	if tipo_entrega not in MULTIPLICADORES_ENTREGA:
		raise ValueError("Tipo de entrega invalido")


def calcular_frete(peso, distancia, tipo_entrega):
	_validar_entrada(peso, distancia, tipo_entrega)

	frete_base = TAXA_BASE + (peso * VALOR_POR_KG) + (distancia * VALOR_POR_KM)
	return frete_base * MULTIPLICADORES_ENTREGA[tipo_entrega]