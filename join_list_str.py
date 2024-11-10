"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
frase = '   Olha só que    ,coisa interessante          '
lista_frases_cruas = frase.split(',')
# limpa_espaco = ' '.join(lista_frases_cruas)


#print(limpa_espaco)
lista_frases = []
'''for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())'''

# ou pode ser assim com o for

for i in lista_frases_cruas: #aqui lista_frases_cruas vai colocando pedaços da lista no i durante a iteraçao
    lista_frases.append(i.strip()) #aqui  o appende vai juntando e colocando dentro de  lista_frases
print(lista_frases)
# print(lista_frases_cruas)
# print(lista_frases)
'''frases_unidas = ', '.join(lista_frases)
print(frases_unidas)'''