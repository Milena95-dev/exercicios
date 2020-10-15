# 13. Ler um número inteiro (assuma até três dígitos) e imprimir a saída da seguinte forma: CENTENA = x DEZENA = x UNIDADE = x

number = str(int(input("Digite um numero: ")))


if len(number)<2:
    unity = print("unidade:", number[0])

elif len(num)< 3:
    ten = print("dezena:", number[0] + "0")
    unity = print("unidade:", number[1])

else:
    hundred = print("centena:", number[0] + "00")
    ten = print("dezena:",number[1]+"0")
    unity = print("unidade:", number[2])


