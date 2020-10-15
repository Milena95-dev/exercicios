# Crie uma lista com 8 valores inteiros. Após, percorrer uma
# lista de forma a verificar o menor e o maior valor.
# Ao final imprima os valores (o maior e o menor)

lista=[]
contador=0
while(contador!= 100):
   contador = int(input("digite os 8 numeros"))
   if (len(lista)<8):
       lista.append(contador)
   else:
       print("Voce excedeu o limite")
       break

print(lista,"lista de numeros")

lista_pares=[]
lista_impares=[]
for n in lista:
    if (n %2 ==0):
        lista_pares.append(n)
    else:
        lista_impares.append(n)
print(lista_pares, "lista de pares", lista_impares, "lista de impares")


