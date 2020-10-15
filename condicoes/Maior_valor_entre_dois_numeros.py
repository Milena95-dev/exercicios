#ler dois valors e comentar o maior deles
n1= int(input("digite um valor"))
n2= int(input("mais um valor"))

if n1>n2:
    print("o numero %d " %n1, "e o maior valor")

if n2>n1:
    print("o numero %d" %n2, "e o maior")

if n1 == n2:
    print( "voce digitou dois numeros iguais")