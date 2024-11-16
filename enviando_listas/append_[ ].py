# Lista original
nove_digitos = [1,2,3,"sonia","marcos"]
# Criação de uma cópia da lista original
dez_digitos = nove_digitos[:]
# Adicionando o primeiro dígito verificador ao final
dez_digitos.append(0)
print(dez_digitos)  # Resultado: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
