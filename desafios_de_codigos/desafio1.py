# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()


# TODO: Aplique o desconto se o cupom for válido:

def calcular_desconto(preco, cupom, tabela_descontos):
    percentual_desconto = tabela_descontos.get(cupom, 0.0)
    valor_do_desconto = preco * percentual_desconto
    return preco - valor_do_desconto

valor_final = calcular_desconto(preco, cupom, descontos)
print(f"{valor_final:.2f}")

