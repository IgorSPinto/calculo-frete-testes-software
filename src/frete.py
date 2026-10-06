TAXA_BASE = 10
VALOR_POR_KG = 2
VALOR_POR_KM = 0.05
MULTIPLICADORES_ENTREGA = {
	"economica": 1.00,
	"padrao": 1.20,
	"expressa": 1.50,
}


def calcular_frete(peso, distancia, tipo_entrega):
	if not 0.1 <= peso <= 30:
		raise ValueError("Peso deve estar entre 0.1 e 30 kg")
	if not 1 <= distancia <= 1000:
		raise ValueError("Distancia deve estar entre 1 e 1000 km")
	if tipo_entrega not in MULTIPLICADORES_ENTREGA:
		raise ValueError("Tipo de entrega invalido")

	frete_base = TAXA_BASE + (peso * VALOR_POR_KG) + (distancia * VALOR_POR_KM)
	return frete_base * MULTIPLICADORES_ENTREGA[tipo_entrega]