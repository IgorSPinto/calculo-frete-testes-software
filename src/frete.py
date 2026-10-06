TAXA_BASE = 10
VALOR_POR_KG = 2
VALOR_POR_KM = 0.05


def calcular_frete(peso, distancia, tipo_entrega):
	frete_base = TAXA_BASE + (peso * VALOR_POR_KG) + (distancia * VALOR_POR_KM)

	if tipo_entrega == "economica":
		return frete_base