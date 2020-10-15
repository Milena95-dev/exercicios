"""
Exercício de Python com (muitos) IF e ELSE
Conforme a tabela dos melhores times de 2019, da CBF,
você deve criar um script que pede
'Digite um número de 1 até 10',
e de acordo com o número fornecido pelo usuário,
indicar qual o time está naquela posição do ranking.
"""
numero=int(input("digite um numero de 1 ate 5: "))

if (numero == 1):
    print('time escolhido, flamengo')
elif(numero ==2):
    print("time escolhido, botafogo")
elif (numero ==3):
    print("time escolhido, fluminense")
elif (numero == 4):
    print("time escolhido, corinthias")
elif (numero ==5):
    print("time escolhido, figueirense")