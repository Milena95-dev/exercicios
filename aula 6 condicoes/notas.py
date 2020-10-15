#Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar: o
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete; o
# A mensagem "Reprovado", se a média for menor do que sete; o
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1=float(input("digite sua primeira nota: "))
nota2=float(input("digite sua segunda nota: "))
total= (nota1+nota2)/2
media=7
if (total<media):
    print("voce foi reprovado!, seu total foi %.2F"%total)
elif (total==media):
    print("voce foi aprovado, seu total foi %.2F"%total, "na media.")
else:
    print("voce foi aprovado com distincao, seu total foi %.2F"%total)