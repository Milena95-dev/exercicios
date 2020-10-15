import math
#40. Faça um algoritmo que receba o valor dos catetos de um triângulo, calcule e mostre o valor da hipotenusa.

#Hipotenusa2 = Cateto oposto2 + Cateto adjacente2

catetoA = float(input("Digite o valor do cateto Adjacente: "))**2

catetoO = float(input("Digite o valor do cateto Oposto: "))**2

soma = catetoA+catetoO

hipotenusa = math.sqrt(soma)

print("Soma dos catetos:", soma,"Resultado:",hipotenusa)



