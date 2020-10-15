#crie um programa que leia o sexo e a idade de varias pessoas, cada uma cadastrada com pergunta.

nome = input("Insira o Nome da pessoa:")
idade= int(input("Agora a idade dela: "))
sexo=input("Seu Gênero: ")
pergunta= input("Deseja Continuar no cadastro?" )

lista_nome = []
lista_idade= []
lista_sexo = []
lista_nome.append(nome)
lista_idade.append(idade)
lista_sexo.append(sexo)

while (pergunta== "sim" ):
    nome = input("Insira o Nome da pessoa:")
    idade= int(input("Agora a idade dela: "))
    sexo=input("Seu Gênero: ")
    pergunta= input("Deseja Continuar no cadastro?")
    lista_nome.append(nome)
    lista_idade.append(idade)
    lista_sexo.append(sexo)
else:
    print(lista_nome, lista_idade, lista_sexo)