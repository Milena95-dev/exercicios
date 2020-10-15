#fazer a contagem de numeros pares de 100 ate 200
num=1
x=100
contador=0
while (x <= 200):
    print(x * num)
    if (x%2==0):
     contador=+1
    x = x + 2

print("a quantidade de pares é", contador)

