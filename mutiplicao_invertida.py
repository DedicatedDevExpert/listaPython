# Lista de números fornecidos
# numeros = [7, 9, 7, 3, 7, 2, 0, 0, 1, 4, 4]
"""numeros = []
soma = 0
cpf = input('informe o CPF:\n >> ' )

# AQUI CONVERTE A  LISTA EM NUMEROS USANDO O LOOP
for i in cpf:
    numeros.append(int(i))

# Lista dos multiplicadores de 10 a 2
multiplicadores = list(range(10, 1, -1))  # [10, 9, 8, 7, 6, 5, 4, 3, 2]

# Usando zip para combinar as listas
combinados = zip(numeros, multiplicadores)

# Multiplicando os elementos correspondentes
resultado = [num * mult for num, mult in combinados]
# soma = sum(resultado)
for valor in resultado: 
    soma +=valor
# Imprimindo o resultado
# print(resultado)
resposta= (soma*10)%11
print(resposta)"""


# SEM USAR O APPEND:

import random

'''cpf = input("Informe o CPF: ")
nove_digitos = cpf[:9]'''


# Inicializar a string para nove_digitos
cpf= ""

# Gerar 9 dígitos aleatórios e armazenar na string
for _ in range(9):
    cpf += str(random.randint(0, 9))

# Converter cada dígito do CPF para inteiro e armazenar em uma lista
numeros = [int(digito) for digito in cpf]

# Lista dos multiplicadores de 10 a 2
multiplicadores = list(range(10, 1, -1))  # [10, 9, 8, 7, 6, 5, 4, 3, 2]

# Usando zip para combinar as listas
combinados = zip(numeros, multiplicadores)

# Multiplicando os elementos correspondentes
resultado = [num * mult for num, mult in combinados]
soma = sum(resultado)

# Imprimindo o resultado
# print(resultado)
#resposta = (soma * 10) % 11
#print(resposta)


digito_1 = (soma * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = cpf + str(digito_1)

# corrigido


"""dez_digitos = nove_digitos + str(
    digito_1
) """


# multiplicadores1 = list(range(11,1,-1))
# combinados = zip(numeros, multiplicadores1)

# corrigido

"""combinados = zip(
    numeros + [digito_1], multiplicadores1
) """

# esse mais o debaixo foi mudado
numeros = [int(digito) for digito in dez_digitos]

multiplicadores1 = list(range(11, 1, -1))

combinados = zip(numeros, multiplicadores1)


resultado = [num * mult for num, mult in combinados]
soma = sum(resultado)

digito_2 = (soma * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado = f"{cpf}{digito_1}{digito_2}"

print(cpf_gerado)

'''if cpf_gerado == cpf:
    print("CPF VALIDO")
else:
    print("CPF INVALIDO")'''


# verificando

"""cpf = input("Informe o CPF: ")
nove_digitos = cpf[:9]

# Converter cada dígito do CPF para inteiro e armazenar em uma lista
numeros = [int(di) for di in nove_digitos]

# Lista dos multiplicadores de 10 a 2
multiplicadores = list(range(10, 1, -1))  # [10, 9, 8, 7, 6, 5, 4, 3, 2]

# Usando zip para combinar as listas
combinados = zip(numeros, multiplicadores)

# Multiplicando os elementos correspondentes
resultado = [num * mult for num, mult in combinados]
soma = sum(resultado)

# Imprimindo o resultado
# print(resultado)
resposta = (soma * 10) % 11
print(resposta)

digito_1 = (soma * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(
    digito_1
)  # Corrigido de 'nove_digitos = str(digito_1)'

multiplicadores1 = list(range(11, 1, -1))
combinados = zip(
    numeros + [digito_1], multiplicadores1
)  # Corrigido para incluir o primeiro dígito verificador

resultado = [num * mult for num, mult in combinados]
soma = sum(resultado)

digito_2 = (soma * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado = f"{nove_digitos}{digito_1}{digito_2}"

if cpf_gerado == cpf:
    print("CPF VALIDO")
else:
    print("CPF INVALIDO")

"""
# testando sequencia

# Criando a lista de 10 a 2
"""sequencia = list(range(10, 1, -1))

# Imprimindo a sequência
print(sequencia)

# Lista de nomes
sequencia = ["marcos", "leonardo", "pedro"]

# Lista dos números decrescentes
sequencia1 = list(range(3, 0, -1))  # [3, 2, 1]

# Combinando as listas usando zip e compreensão de lista
combinados =zip(sequencia,sequencia1)

#resultado = [(nome,num) for nome,num in zip(sequencia,sequencia1)]
resultado = [(nome,num) for nome,num in combinados]


# Imprimindo o resultado
print(resultado)"""


# converter zip em list


# Listas de exemplo
"""numeros = [7, 9, 7, 3, 7, 2, 0, 0, 1, 4, 4]
multiplicadores = list(range(10, 1, -1))  # [10, 9, 8, 7, 6, 5, 4, 3, 2]

# Usando zip com parênteses corretos
combinados = zip(numeros, multiplicadores)

# Convertendo o objeto zip em uma lista para visualização
resultado = list(combinados)

# Imprimindo o resultado
print(resultado)"""
