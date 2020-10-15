'''7. Entrar com o dia e o mês de uma data e informar quantos dias se passaram desde o início do
ano. Esqueça a questão dos anos bissextos e considere sempre que um mês possui 30 dias.'''

day = int(input("digite um dia: "))
month = int(input("digite um mes: "))

if month > 1:
    total = (month-1)*30+day

else:
    total = day

print("já se passaram:",total,"dias.")
