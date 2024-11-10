import os

lista = []

while True:
    print("Selecione a sua opçao: ")
    opcao = input("[i]inserir [a]apagar [l]listar \n>> ")

    if opcao == "i":
        os.system("cls")
        valor = input("Valor: ")
        lista.append(valor)
    elif opcao == "a":
        indice_str = input("Escolha o índice para apagar: ")
        try:
            indice = int(indice_str)
            del lista[indice]

        except ValueError:
            print("Por favor digite numeros inteiros")
        except IndexError:
            # print('Por favor digite o indice ')
            print(
                f"Índice inválido: {indice}. O índice deve estar entre 0 e {len(lista)-1}."
            )
    elif opcao == "l":
        if len(lista) == 0:
            print("nao tem nada para listar! ")
        for i, valor in enumerate(lista):
            print(i, valor)

    else:
        print("por favor escolha a opcao correta! ")
