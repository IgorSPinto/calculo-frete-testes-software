def calcular_frete(peso, distancia, tipo_entrega):
	frete_base = 10 + (peso * 2) + (distancia * 0.05)

	if tipo_entrega == "economica":
		return frete_base