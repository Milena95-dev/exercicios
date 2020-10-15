#Cabeçalho
print ("*"*16, "FACULDADE CESUSC","*"*16 )
print("* Curso: Análise e Desenvolvimento de Sistemas    *")
print("* Aluno: Milena Pereira Torres ")
print("* Professor: Roberto Fabiano Fernandes      *")
print("*"*40)

#importei as funções da lista ordenada na pasta chamada N2.
from n2 import func_da_lista_ordenada


#Importei a função random para fazer a lista aleatória de números.
import random

#Criei a variável de letra A, a lista alfanumérica vazia e a lista de números aleatória gerando uma sequência aleatória a partir do tamanho que eu escolhi,
#sendo 101 (sendo considerado -1).
letra = "A"
lista_alfanumerico = []
lista_de_numeros = random.sample(range(0, 101),101) #gera uma lista aleatória de números entre 0 e 100 e tamanho até 100.(está em 101 pois o tamanho final é -1)

#Imprimi a lista fora de ordem para mostrar a lista original.
print("Lista desordenada: ", lista_de_numeros)


#Programa Principal
#Para cada elemento na função ordenar da lista ordenada, atribui uma variável alfanumerico que eu criei e juntei a variavel letra + string
# (o elemento transformado em texto),depois adicionei a lista alfanumerica cada elemento com a letra junta.
for elemento in func_da_lista_ordenada.ordenar(lista_de_numeros):
    alfanumerico = letra+ str(elemento) # 0 ; 1 ;2 : a0, a1, a2
    lista_alfanumerico.append(alfanumerico)


# aqui apenas chamei a função imprir também da lista ordenada.
func_da_lista_ordenada.imprimir(lista_alfanumerico)

#fim
