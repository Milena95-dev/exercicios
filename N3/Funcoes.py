
def cabecalho():
    print("*" * 16, "FACULDADE CESUSC", "*" * 16)
    print("* Curso: Análise e Desenvolvimento de Sistemas    *")
    print("* Aluno: Milena Pereira Torres ")
    print("* Professor: Roberto Fabiano Fernandes      *")
    print("*" * 40)
###########################################################################

def menu():
    print("""Escolha a opção:
          1 - Cadastrar 
          2 - Listar Dados
          3 - Alterar Dados
          4 - Excluir Dados
          5 - Realizar Cópia do arquivo
          0 - Sair"
          Digite a opção escolhida: """)
    return input()

#Escolha de opções
############################################################################
def menu_opcoes():
    while True:
        opcao = menu()
        if opcao == '1':
            cadastro()
        elif opcao == '2':
            listar()
        elif opcao == '3':
            dado = input("Insira o nome do dado que deseja alterar: ")
            alterar(dado)
        elif opcao == '4':
            dado = input("Insira o nome do dado que queira excluir: ")
            excluir(dado)
        elif opcao == '5':
            copia()
        else:
            print("Programa Encerrado.")
            break
###################################################
def cadastro():

 try:
     doencas = ['Respiratória', 'Cardiovascular', 'Diabetes', 'Hipertensão']

     nome=''
     cartao_nacional_de_saude=''
     bairro=''
     unidade_de_saude=''
     idade=''
     comorbidade=''
     data_de_inicio_dos_sintomas=''
     endereco=''
     telefone1=''
     telefone2=''
     sintomas_iniciais=''

     arquivo= open('arquivo_de_dados.txt','a')
     nome = input("Digite seu nome: ")
     cartao_nacional_de_saude = input("Digite os números do seu CNS: ")
     bairro = input("Digite seu bairro: ")
     unidade_de_saude = input("Digite a unidade de saúde: ")
     idade = input("Qual sua data de nascimento:")
     comorbidade = input("Possui alguma doença Respiratória? Cardiovascular? Diabetes? Hipertensão? Escreva quais possui, se não, apenas digite 'nenhuma'. ")
     if(comorbidade.capitalize() in doencas):
         data_de_inicio_dos_sintomas = input("Qual data começou os sintomas?")

     endereco = input("Digite o Endereço completo: ")
     telefone1 = input("Insira um telefone para continuar: ")
     telefone2 = input("Insira outro telefone. *Opcional* ")
     sintomas_iniciais = input("Teve algum destes sintomas: FEBRE, TOSSE, DOR DE GARGANTA, CORIZA, DIFICULDADE RESPIRATÓRIA? Se sim, diga quais: ")
     arquivo.writelines(['Nome: ' + nome+'\n',
                         'CNS: ' + cartao_nacional_de_saude+'\n',
                         'Bairro: ' + bairro + '\n',
                         'Unidade de saúde: ' + unidade_de_saude + '\n',
                         'Idade: ' + idade + '\n',
                         'Comorbidade: ' + comorbidade + '\n',
                         'Início dos sintomas: ' + data_de_inicio_dos_sintomas + '\n',
                         'Endereço: ' + endereco + '\n',
                         'Telefone 1: ' + telefone1 + '\n',
                         'Telefone 2: ' + telefone2 + '\n',
                         'Sintomas iniciais: ' + sintomas_iniciais + '\n',
                         '\n',
                         '########################################################\n',
                         '\n'])

     arquivo.close()

     pergunta= input("Deseja cadastrar mais pessoas?")
     while (pergunta != 'não'.casefold() and pergunta != 'sim'.casefold()):
            print(" ")
            print("Resposta inválida!")
            print(" ")
            pergunta= input("Deseja cadastrar mais pessoas?")


     if pergunta.casefold() == "sim".casefold():
        cadastro()
     else:
        print(" ")
        print("Cadastro concluído", "\n")
 except IOError as error:
     print("Erros registrados", error)


#############################################################
def listar():
    try:
        arquivo = open("arquivo_de_dados.txt",'r')
        print('Lista:', '\n')
        print('------------------------------')
        print(arquivo.read())
        arquivo.close()
        input("Pressione 'Enter' para voltar ao menu")
        menu_opcoes()
    except IOError as error:
        print("Erro encontrado" , error)
###############################################################
def alterar(dado):
    try:
        with open("arquivo_de_dados.txt",'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                if linha.casefold().startswith(dado.casefold()):
                 novo_dado= input("insira um novo dado para " + dado + ": ")
                 pos = linhas.index(linha)
                 linhas.pop(pos)
                 item = dado.capitalize()+ ': ' + novo_dado + '\n'
                 linhas.insert(pos, item)
                 arquivo = open("arquivo_de_dados.txt", 'w')
                 arquivo.writelines(linhas)
                 arquivo.close()
                 print("Cadastro alterado!")
                 input("Pressione 'Enter' para voltar ao menu")
                 menu_opcoes()
        print("Cadastro não encontrado")

    except IOError as error:
     print("ERRO:", error)

############### ###########################################################
def excluir(dado):
    dado_para_remover = dado.capitalize()
    try:
        with open('arquivo_de_dados.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                if(linha.casefold().startswith(dado_para_remover.casefold())):

                    pos = linhas.index(linha)
                    linhas.pop(pos)
                    arquivo = open('arquivo_de_dados.txt','w')
                    arquivo.writelines(linhas)
                    arquivo.close()
                    print("Dado removido.")
                    input("Pressione 'Enter' para voltar ao menu")
                    menu_opcoes()
            print("Cadastro não encontrado!")
    except IOError as error:
        print("ERRO:", error)
 #####################################################################

def copia():
    try:
        arquivo1 = open('arquivo_de_dados.txt', 'r')
        arquivo2 = open('copia_de_dados.txt', 'w')
        for texto in arquivo1:
            arquivo2.writelines(texto)
        arquivo1.close()
        arquivo2.close()
        print("Cópia feita.")
    except IOError as error:
        print("ERRO:", error)




