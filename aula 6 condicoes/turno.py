#Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!",
# conforme o caso.

m = "m"
v ="v"
n ="n"

x=input("digite qual seu turno, sendo que m-matutino, v-vespertino e n-noturno ")

if (x==m):
    print("bom dia")
elif (x==v):
    print("boa tarde")
elif (x==n):
    print("boa noite")
