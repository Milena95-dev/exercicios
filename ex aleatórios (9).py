'''4. Escreva um algoritmo para ler o nome e a idade de uma pessoa, e exibir quantos dias de
vida ela possui. Considere sempre anos completos, e que um ano possui 365 dias. Ex: uma
pessoa com 19 anos possui 6935 dias de vida; veja um exemplo de saída: MARIA, VOCÊ JÁ
VIVEU 6935 DIAS 5.'''

name = input("digite seu nome:");
age = int(input("digite sua idade:"));
year = 365
total = age*year

print('Nome:', name, '/ idade:', age,'/ Dias vividos:', total)