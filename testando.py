'''lista = [1,3,7,6,5,2,4,8,9]

multiplicadores = list(range(9,1,-1))
multiplica = zip(multiplicadores,lista)

resultado = [numero * mult for numero,mult in multiplica]

print(resultado)'''

# OUTRA FORMA

'''cpf = "79737200144"
nove_digito = cpf[:9]
contagem_regressiva = 10
soma = 0
# print(nove_digito)

for digito in nove_digito:
    digito = int(digito)
    print(digito*contagem_regressiva)
    multi = digito*contagem_regressiva
    #print(multi)
    soma +=multi

    contagem_regressiva-= 1
print("soma", soma)'''


# outra forma de usar o for nessa contagem, enumerate
'''cpf = "79737200144"
nove_digito = cpf[:9]
contagem_regressiva = 10
soma = 0

for i, digito in enumerate(nove_digito):
    digito = int(digito)
    print(f'{digito} X {contagem_regressiva - i} = {digito*(contagem_regressiva -i)}')'''


# outra forma com range(len())

'''cpf = "79737200144"
nove_digito = cpf[:9]
contagem_regressiva = 10
soma = 0

for i in range(len(nove_digito)):
    digito = int(nove_digito[i])
    print(f'{digito} X {contagem_regressiva - i} = {digito * (contagem_regressiva - i)}')'''


# outra forma:


'''cpf = "79737200144"
nove_digito = cpf[:9]
contagem_regressiva = 10

# Combina os índices com os dígitos


for i, digito in zip(range(len(nove_digito)), nove_digito):
    digito = int(digito)
    print(
        f"{digito} x {contagem_regressiva - i} = {digito * (contagem_regressiva - i)}"
    )'''
"""Explicação:
range(len(nove_digito)):

Gera uma sequência de números de 0 a 8 (os índices dos caracteres de nove_digito).

Exemplo: [0, 1, 2, 3, 4, 5, 6, 7, 8].

nove_digito:

A string com os primeiros 9 dígitos do CPF, por exemplo, "797372001".

zip(range(len(nove_digito)), nove_digito):

Combina os índices gerados pelo range com os caracteres da string.

Exemplo de pares gerados pelo zip: [(0, '7'), (1, '9'), (2, '7'), (3, '3'), (4, '7'), (5, '2'), (6, '0'), (7, '0'), (8, '1')]."""


# OUTRA FORMA USANDO LIS E MAP

'''cpf = "79737200144"
nove_digito = cpf[:9]
contagem_regressiva = 10

# Mapeia cada caractere da string para um inteiro
digitos = list(map(int, nove_digito))

for i, digito in enumerate(digitos):
    print(
        f"{digito} x {contagem_regressiva - i} = {digito * (contagem_regressiva - i)}"
    )'''

# outra forma

# cpf = "74682489070"
'''cpf_enviado_usuario = "79737200144"
nove_digitos = cpf_enviado_usuario[:9]
contagem_regressiva = 10
soma = 0
resultado = 0

for digito in nove_digitos:
    resultado+= int(digito)* contagem_regressiva
    contagem_regressiva-=1
digito = (resultado*10)%11
digito = digito if digito <=9 else 0
print(digito)'''


# com Dez Digitos

cpf_enviado_usuario = "79737200144"
nove_digitos = cpf_enviado_usuario[:9]

contagem_regressiva_1 = 10
soma = 0
resultado_digito_1 = 0

for digito in nove_digitos: 
    resultado_digito_1 += int(digito)*contagem_regressiva_1
    contagem_regressiva_1 -= 1

digito_1 = (resultado_digito_1 * 10)%11
digito_1 = digito_1 if digito_1 <=9 else 0


dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11
# print(dez_digitos)

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2+=(int(digito)* contador_regressivo_2)
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10)%11
digito_2 = digito_2 if digito_2 <= 9 else 0
# print(resultado)

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'
if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_usuario} é válido')
else:
    print(f'CPF inválido')
