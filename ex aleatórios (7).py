#37. Faça um algoritmo que calcule e mostre a tabuada de um número digitado pelo usuário.
tabuada = int(input("escolha um número para fazer sua tabuada: "))
x = 0
print('Tabuada de {}'.format(tabuada))
while(x <= 10):
  print('{0} X {1} = {2}'.format(x, tabuada, (x * tabuada)))
  x = x + 1