#print("valor" if False else "outro-valor" if False else "fim")


# Caso 1: digito_1 é 7 (menor ou igual a 9)
digito_1 = 7
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)  # Saída: 7

# Caso 2: digito_1 é 12 (maior que 9)
digito_1 = 12
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)  # Saída: 0
 