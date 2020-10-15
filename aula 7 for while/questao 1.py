#cabeçalho:
print ("*"*16, "FACULDADE CESUSC","*"*16 )
print("* Curso: Análise e Desenvolvimento de Sistemas    *")
print("* Aluno: Milena Pereira Torres ")
print("* Professor: Roberto Fabiano Fernandes      *")
print("*"*40)

#variavel com nome cadastro declarada como string, 3 listas vazias de aluno para o nome, nota e frenquencia (falta):
cadastro="sim"
lista_alunos=[]
lista_de_notas=[]
lista_de_frequencia=[]


#o while com condição que enquanto cadastro for igual a sim, ele pergunta o nome a ser digitado, as 4 notas, a frequencia, faz a média das notas, adiciona
#cada nome, frequencia e a média das notas em suas respectivas listas e pergunta se deseja cadastrar mais alunos:
while (cadastro=="sim"):
    nome=input("Digite o nome do Aluno: ")
    nota1=float(input("digite a primeira nota: "))
    nota2=float(input("digite a segunda nota: "))
    nota3=float(input("digite a terceira nota: "))
    nota4=float(input("digite a quarta nota: "))
    frequencia=int(input("qual foi sua frquencia?"))
    media_das_notas=(nota1+nota2+nota3+nota4)/4
    lista_alunos.append(nome)
    lista_de_frequencia.append(frequencia)
    lista_de_notas.append(media_das_notas)
    cadastro = input("deseja cadastrar mais um aluno?")

#variavel chamada contador zerada.
contador=0

#regras de aprovação, recuperação e reprovação dos alunos, mostrando seus nomes, notas e frequência, ao final do looping, o contador se soma garantindo
#a passagem por todos os elementos das outras listas:
for x in lista_alunos:

    if (lista_de_notas[contador]>= 6 and lista_de_frequencia[contador]<=10):
     print()
     print(x," passou direto, sua media foi %.2F"%lista_de_notas[contador],"e teve frquencia igual a", lista_de_frequencia[contador])

    elif(lista_de_notas[contador] >= 6 and lista_de_frequencia[contador] > 10):
     print()
     print(x," ficou em recuperacao devido a sua frenquencia: ", lista_de_frequencia[contador])

    elif(lista_de_notas[contador]>4 and lista_de_notas[contador]<6):
     print()
     print(x," ficou em recuperacao por nota, sendo sua nota:%.2F"%lista_de_notas[contador])

    elif(lista_de_notas[contador]<=4):
     print()
     print(x," foi reprovado, repetira de ano por sua nota nao ser suficiente, sendo ela: %.2F"%lista_de_notas[contador])

    elif(lista_de_frequencia[contador] > 10):
     print()
     print(x," excedeu o limite de faltas e nao possui nota suficiente para recuperacao, portanto repetira de ano, sua nota e frequencia sao: %.2F"%lista_de_notas[contador], lista_de_frequencia[contador])
     contador+=1

#imprime as respectivas listas:
print()
print("nomes: ",lista_alunos)
print("notas: ",lista_de_notas)
print("frequencia: ", lista_de_frequencia)

