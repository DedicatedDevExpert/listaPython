item1 = (1, 2, 3)  # Isto é uma tupla

if isinstance(item1, tuple):
    print("Item1 é uma tupla!")
else:
    print("Item1 não é uma tupla.")

item2 = [1, 2, 3]  # Isto é uma lista

if isinstance(item2, list):
    print("Item2 é uma lista!")
else:
    print("Item2 não é uma lista.")


item3 = {"chave": "valor"}  # Isto é um dicionário

if isinstance(item3, dict):
    print("Item3 é um dicionário!")
else:
    print("Item3 não é um dicionário.")
