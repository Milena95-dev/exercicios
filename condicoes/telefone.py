#Calcular a conta de um telefone celular da empresa Tchau.
#Os planos da empresa são bem interessantes e oferecem preços diferenciados com a
#quantidade de minutos usados por mês. Abaixo de 200 minutos, a empresa cobra R$ 0,20 por minuto.
#Entre 200 e 400 minutos, o preço é de R$ 0,18. Acima de 400 minutos,
#o preço por minuto é de R$ 0,15.

duzentos=0.20
entre_os_dois_valores=0.18
quatrocentos=0.15

tempo_gasto= float(input("digite a quantidade de minutos gastos: "))
if (tempo_gasto <= 200):
    print(" voce gastou %.2f"%duzentos,"centavos")

elif (tempo_gasto>201 and tempo_gasto<=400):
    print("voce gastou %.2f"%entre_os_dois_valores, "centavos")

else:
    print("voce gastou %.2f"%quatrocentos, "centavos")

