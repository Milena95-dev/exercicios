'''27. Faça um algoritmo que receba dois números, calcule e mostre a divisão do primeiro número pelo segundo.
Sabe-se que o segundo número não pode ser zero, portanto não é necessário se preocupar com validações.'''

num1 = int(input("diga o primeiro numero: "))
num2 = int(input("agora diga o segundo: "))

if num2 >0:
    divisao = num1/num2
    print(divisao)

else:
    print("Erro, 0 não incluso")