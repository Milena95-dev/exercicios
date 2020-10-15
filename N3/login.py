from Funcoes import *
def login():
     user= input("Digite seu login: ")
     password=input("Digite sua senha: ")

     if(not validateLogin(user, password)):
         print(' ')
         print('####### Dados incorretos #########')
         login()
     else:
         print(' ')
         print("Login realizado com sucesso")
         input("Pressione 'Enter' para continuar")
         menu_opcoes()


def validateLogin(user, password):

    server = open('login_e_senha.txt')
    lines = server.readlines()
    is_valid = user in lines[0] and password in lines[1]
    server.close()
    return is_valid

login()


