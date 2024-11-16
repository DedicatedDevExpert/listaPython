'''string = 'ABC'
lista = ["Maria","Rogerio",1,2,3,"Pedro"]

print(*lista)
print(*string)'''


salas = [
    ["Maria", "Helena"],  # 0
    ["Elaine"],  # 1
    ["Luiz", "João", "Eduarda", (0, 10, 20, 30, 40)],  # 2
]

#print(*salas,sep="\n")

print("Maria", "Helena", "Elaine", sep="-", end="!")
# Saída: Maria-Helena-Elaine!
