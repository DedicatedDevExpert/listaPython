"""
Lista de listas e seus índices
"""

'''salas = [
    # 0        1
    [
        "Maria",
        "Helena",
    ],  # 0
    # 0
    [
        "Elaine",
    ],  # 1
    # 0       1       2
    [
        "Luiz",
        "João",
        "Eduarda",
        (0,10,20,30,40)
    ],  # 3
]
print(salas[2][3][3])
# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][3])
# print(salas)
# print([2][3][3])'''

'''for sala in salas:
    #print(f"A sala é {sala}")
    for aluno in sala:
       # print(aluno)
        for item in aluno:
            print('item',item,end='')'''

salas = [
    ["Maria", "Helena"],  # 0
    ["Elaine"],  # 1
    ["Luiz", "João", "Eduarda", (0, 10, 20, 30, 40)],  # 2
]

# Primeiro for: iterar sobre cada sala
for sala in salas:
    # Segundo for: iterar sobre cada item dentro da sala
    for item in sala:
        # Terceiro for: se o item for uma tupla, iterar sobre os elementos da tupla
        if isinstance(item, tuple):
            for numero in item:
                print(numero)
# Simples
'''salas = [
    ["Maria", "Helena"],  # 0
    ["Elaine"],  # 1
    ["Luiz", "João", "Eduarda", (0, 10, 20, 30, 40)],  # 2
]

# Acessa diretamente a tupla na lista de salas
tupla = salas[2][3]

# Itera sobre os elementos da tupla
for numero in tupla:
    print(numero)'''

# mais complexo

'''salas = [
    ["Maria", "Helena"],  # 0
    ["Elaine"],  # 1
    ["Luiz", "João", "Eduarda", (0, 10, 20, 30, 40)],  # 2
]

# Primeiro for: iterar sobre cada sala
for i in range(len(salas)):
    # Segundo for: iterar sobre cada item dentro da sala
    for j in range(len(salas[i])):
        # Terceiro for: iterar sobre os elementos da tupla, garantindo que estamos no índice correto
        if i == 2 and j == 3:
            #for numero in salas[i][j]:
                #print(numero)
                print(salas[i][j][2])'''
