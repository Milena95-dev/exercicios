'''8. Faça um algoritmo para ler três notas de um aluno em uma disciplina e imprimir a sua média
ponderada (as notas tem pesos respectivos de 1, 2 e 3).'''

nota01 = float(input("digite a primera nota: "));
nota02 = float(input("digite a segunda nota: "));
nota03 = float(input("digite a terceira nota: "));

calculo = (nota01*1) + (nota02*2) + (nota03*3)/6
media = calculo/6

print("Sua média ponderada é: %2.2f" %media)