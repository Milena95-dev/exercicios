#cabeçalho:
print ("*"*16, "FACULDADE CESUSC","*"*16 )
print("* Curso: Análise e Desenvolvimento de Sistemas    *")
print("* Aluno: Milena Pereira Torres ")
print("* Professor: Roberto Fabiano Fernandes      *")
print("*"*40)

#criação de lista geral e de números pares:
lista = []
lista_de_pares=[]

#input para digitar a lista de números:
i = int(input("Digite um número da lista: "))

#o while está com a condição de que enquanto a variável i for diferente de -1, adicionará à lista e perguntará novamente outro número:
while (i!=-1):
    lista.append(i)
    i = int(input("Digite um número da lista: "))

#imprime na tela a lista de números pares:
print("Os seguintes números da lista são pares: ")

#o for passa por cada elemento da lista e caso  o resto da divisão desse elemento por 2 for igual a 0, ele é par e é adicionado na lista de pares:
for n in lista:
    if(n%2==0):
     lista_de_pares.append(n)

#imprime a lista de pares:
print(lista_de_pares)

