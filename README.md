# Cálculo de Frete — Testes de Software

## Sobre o projeto

Módulo desenvolvido para a disciplina de Testes de Software do Bacharelado em Ciência da Computação do IFPR Campus Pinhais, como atividade teórico-prática de certificação/aproveitamento de conhecimentos.

O objetivo é calcular o frete por peso, distância e tipo de entrega, aplicando TDD (desenvolvimento orientado por testes) e técnicas de teste de software. A função principal é `calcular_frete(peso, distancia, tipo_entrega)`. As validações ficam na função auxiliar privada `_validar_entrada`, e os valores fixos, limites e multiplicadores são definidos em constantes.

## Regras de negócio

1. A taxa base do frete é R$ 10,00.
2. O peso válido está entre 0,1 kg e 30 kg, inclusive.
3. A distância válida está entre 1 km e 1000 km, inclusive.
4. O valor base é calculado por `10 + (peso * 2) + (distancia * 0.05)`, com R$ 2,00 por kg e R$ 0,05 por km.
5. Os tipos de entrega aceitos são `economica` (multiplicador 1.00), `padrao` (1.20) e `expressa` (1.50).
6. Peso ou distância fora dos intervalos válidos, ou tipo de entrega não aceito, geram `ValueError`.

## Fórmula do cálculo

```python
frete_base = 10 + (peso * 2) + (distancia * 0.05)
frete_final = frete_base * multiplicador
```

O peso é informado em kg e a distância em km. O multiplicador é escolhido conforme o tipo de entrega:

| Tipo | Multiplicador | Acréscimo sobre o valor base |
| --- | --- | --- |
| `economica` | 1.00 | Sem acréscimo |
| `padrao` | 1.20 | 20% |
| `expressa` | 1.50 | 50% |

## Tecnologias utilizadas

- Python 3.12: linguagem de implementação.
- pytest: execução dos testes unitários e parametrizados.
- pytest-cov: medição da cobertura de código.
- Git: controle de versão e registro dos ciclos TDD.
- GitHub: hospedagem do repositório.

## Estrutura do projeto

```text
calculo-frete-testes-software/
├── src/
│   ├── __init__.py
│   └── frete.py
├── tests/
│   ├── __init__.py
│   └── test_frete.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Instalação

Com Python 3.12 e Git disponíveis, execute:

1. Clone o repositório e entre na pasta:

	```bash
	git clone https://github.com/IgorSPinto/calculo-frete-testes-software.git
	cd calculo-frete-testes-software
	```

2. Opcionalmente, crie e ative um ambiente virtual. No Windows, usando PowerShell:

	```powershell
	python -m venv .venv
	.\.venv\Scripts\Activate.ps1
	```

3. Instale as dependências:

	```bash
	pip install -r requirements.txt
	```

## Execução dos testes

Na raiz do projeto, execute:

```bash
python -m pytest
```

## Cobertura de código

```bash
python -m pytest --cov=src --cov-report=term-missing
```

A suíte atual alcança 100% de cobertura de linhas em `src/frete.py` e no total de `src`. O relatório também indica as linhas não executadas. Cobertura de 100% não garante ausência de defeitos: ela não comprova que todas as entradas, combinações e comportamentos possíveis foram verificados.

## Estratégia de testes

- **Testes unitários:** verificam o cálculo e as validações da função principal de forma isolada, sem serviços externos.
- **Particionamento de equivalência:** considera entradas válidas e inválidas para peso e distância, além dos tipos de entrega aceitos e de um tipo não aceito.
- **Análise de valor limite:** verifica os extremos válidos (0,1 e 30 kg; 1 e 1000 km) e valores fora desses intervalos.
- **Testes parametrizados:** usam `pytest.mark.parametrize` para executar a mesma verificação com diferentes dados, evitando duplicação.
- **Validação de entradas inválidas:** usa `pytest.raises(ValueError)` para verificar a exceção esperada.

## Desenvolvimento com TDD

Os três ciclos Red-Green-Refactor estão registrados no histórico do Git. Após os ciclos, a suíte foi reorganizada com parametrização e ampliada para reforçar a análise de valor limite, sem criar um novo ciclo TDD.

### Ciclo 1

- **RED:** criação do teste inicial do frete econômico, com falha por ausência da função.
- **GREEN:** implementação do cálculo básico para aprovar o teste.
- **REFACTOR:** extração dos valores fixos do cálculo para constantes.

### Ciclo 2

- **RED:** adição dos testes das entregas padrão e expressa, inicialmente com falhas.
- **GREEN:** implementação dos multiplicadores dos novos tipos de entrega.
- **REFACTOR:** centralização dos multiplicadores no dicionário `MULTIPLICADORES_ENTREGA`.

### Ciclo 3

- **RED:** adição dos testes de peso, distância e tipo de entrega inválidos.
- **GREEN:** implementação das validações com `ValueError`.
- **REFACTOR:** extração das validações para `_validar_entrada` e dos limites para constantes.

## Exemplos de uso

Com o Python iniciado na raiz do projeto:

```pycon
>>> from src.frete import calcular_frete
>>> calcular_frete(5, 100, "economica")
25.0
>>> calcular_frete(5, 100, "padrao")
30.0
>>> calcular_frete(5, 100, "expressa")
37.5
```

Uma entrada com peso abaixo do mínimo gera `ValueError`:

```pycon
>>> calcular_frete(0.09, 100, "economica")
Traceback (most recent call last):
	 ...
ValueError: Peso deve estar entre 0.1 e 30 kg
```

## Resultados

- 14 casos de teste coletados pelo pytest.
- Todos aprovados no estado final.
- Cobertura de linhas de 100% no módulo e no total de `src`.

## Limitações

Este é um módulo acadêmico simplificado. Não considera CEP, transportadora real, dimensões da embalagem, peso cúbico, pedágios, seguro, prazo real de entrega ou rastreamento.

## Possíveis melhorias

- Integração com API e desenvolvimento de interface gráfica.
- Cálculo por CEP/região, inclusão de peso cúbico e suporte a múltiplas transportadoras.
- Testes de integração, de sistema e de desempenho.

## Autor

Igor de Souza Pinto