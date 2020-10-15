""" Tendo como dados de entrada a distância total (em km) percorrida por um automóvel e a
quantidade de combustível (em litros)
consumida para percorrê-la, calcule e imprima o consumo médio de combustível. """

quantidade_em_litros= float(input("insira agora a quantidade em litros: "))
distancia_total = float(input("insira a distancia total percorrida: "))
consumo_medio= (distancia_total/quantidade_em_litros)

print("o seu carro percorreu %.2f Km/litro"%consumo_medio,"de litros")

if (consumo_medio <= 5):
    print("seu carro esta bem")
elif(consumo_medio ==6):
    print("seu carro esta quase explodindo")
else:
    print("seu carro explodiu!")


