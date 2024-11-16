import random

'''# Gerar 9 dígitos aleatórios e armazenar em uma lista
nove_digitos = [random.randint(0, 9) for _ in range(9)]

# Lista dos multiplicadores de 10 a 2 para o primeiro dígito verificador
multiplicadores = list(range(10, 1, -1))  # [10, 9, 8, 7, 6, 5, 4, 3, 2]

# Usando zip para combinar as listas
combinados = zip(nove_digitos, multiplicadores)

# Multiplicando os elementos correspondentes
resultado = [num * mult for num, mult in combinados]
soma = sum(resultado)

# Calcular o primeiro dígito verificador
digito_1 = (soma * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

# Adicionar o primeiro dígito verificador aos nove primeiros dígitos
dez_digitos = nove_digitos + [digito_1]

# Lista dos multiplicadores de 11 a 2 para o segundo dígito verificador
multiplicadores = list(range(11, 1, -1))  # [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

# Usando zip para combinar as listas
combinados = zip(dez_digitos, multiplicadores)

# Multiplicando os elementos correspondentes
resultado = [num * mult for num, mult in combinados]
soma = sum(resultado)

# Calcular o segundo dígito verificador
digito_2 = (soma * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

# Adicionar o segundo dígito verificador à lista
cpf = dez_digitos + [digito_2]

# Converter de volta para string para exibição
cpf_str = "".join(map(str, cpf))

print("CPF completo:", cpf_str)


# OUTRA FORMA DE GERAÇÃO  DE CPF'''




# Inicializar a string para nove_digitos
nove_digitos = ""

# Gerar 9 dígitos aleatórios e armazenar na string
for _ in range(9):
    nove_digitos += str(random.randint(0, 9))

# Converter cada dígito do CPF para inteiro e armazenar em uma lista
numeros = [int(digito) for digito in nove_digitos]

# Lista dos multiplicadores de 10 a 2
multiplicadores = list(range(10, 1, -1))  # [10, 9, 8, 7, 6, 5, 4, 3, 2]

# Usando zip para combinar as listas
combinados = zip(numeros, multiplicadores)

# Multiplicando os elementos correspondentes
resultado = [num * mult for num, mult in combinados]
soma = sum(resultado)

# Calcular o primeiro dígito verificador
digito_1 = (soma * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

# Adicionar o primeiro dígito verificador à string nove_digitos
dez_digitos = nove_digitos + str(digito_1)

# Imprimir resultados para verificação
print("Primeiro dígito verificador:", digito_1)
print("Dez primeiros dígitos:", dez_digitos)
