

#Pedir ao usuário que introduza 5 números.
#Guardar em uma lista. Mostrar a lista.
#1ªforma de resolver sem FOR, só com métodos das listas


lista = []

while (len(lista)< 5):
    numeros= int(input("digite 5 numeros"))
    lista.append(numeros)
print(lista)

