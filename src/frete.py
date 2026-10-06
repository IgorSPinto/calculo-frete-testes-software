TAXA_BASE = 10
VALOR_POR_KG = 2
VALOR_POR_KM = 0.05
MULTIPLICADORES_ENTREGA = {
	"economica": 1.00,
	"padrao": 1.20,
	"expressa": 1.50,
}


def calcular_frete(peso, distancia, tipo_entrega):
	frete_base = TAXA_BASE + (peso * VALOR_POR_KG) + (distancia * VALOR_POR_KM)
	return frete_base * MULTIPLICADORES_ENTREGA[tipo_entrega]