#Pedir ao usuário que introduza 5 números. Guardar em uma lista. Mostrar a lista.2ªforma de resolver
#Utilize um FOR

list = []
numbers = 0
numbers = int(input("digite 5 numeros"))
list.append(numbers)

for n in list:
    if (len(list)< 5):
     numbers = int(input("digite 5 numeros"))
     list.append(numbers)

print(list)