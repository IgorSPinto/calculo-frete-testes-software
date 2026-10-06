TAXA_BASE = 10
VALOR_POR_KG = 2
VALOR_POR_KM = 0.05
MULTIPLICADOR_ECONOMICA = 1.00
MULTIPLICADOR_PADRAO = 1.20
MULTIPLICADOR_EXPRESSA = 1.50


def calcular_frete(peso, distancia, tipo_entrega):
	frete_base = TAXA_BASE + (peso * VALOR_POR_KG) + (distancia * VALOR_POR_KM)

	if tipo_entrega == "economica":
		return frete_base * MULTIPLICADOR_ECONOMICA
	if tipo_entrega == "padrao":
		return frete_base * MULTIPLICADOR_PADRAO
	if tipo_entrega == "expressa":
		return frete_base * MULTIPLICADOR_EXPRESSA