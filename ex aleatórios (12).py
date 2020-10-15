#11. Uma fábrica controla o tempo de trabalho sem acidentes pela quantidade de dias.
# Faça um algoritmo para converter este tempo em anos, meses e dias. Assume que cada mês possui sempre 30 dias.

time = int(input("digite o tempo sem acidentes: "))

month = tempo / 30

years = tempo / 365

days_left = 0

if(mes >= 1):
    days_left = tempo - (int(mes) * 30)
else:
    days_left = tempo



print("Dias: %.2f" %time, "Mes: %.2f" %month,"Ano: %.2f"%years)