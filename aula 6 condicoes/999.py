contador1=0

lista_de_numeros=[]

while(contador1!=999):
     contador1 = int(input("digite os numeros que quiser"))
     if (contador1!=999):
      lista_de_numeros.append(contador1)

print(len(lista_de_numeros),"Numeros Digitados")

controlador=0
soma = 0

for n in lista_de_numeros:

  soma += lista_de_numeros[controlador]

  controlador+=1

print(soma, "soma dos numeros")