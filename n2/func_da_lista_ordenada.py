#Cabeçalho
print ("*"*16, "FACULDADE CESUSC","*"*16 )
print("* Curso: Análise e Desenvolvimento de Sistemas    *")
print("* Aluno: Milena Pereira Torres ")
print("* Professor: Roberto Fabiano Fernandes      *")
print("*"*40)

#Criei uma função chamada ordenar que recebe uma lista como parâmetro, criei uma variável "nova lista" para ser retornada da função e uma variável "término",
#que pega o tamanho total da lista.

# Fiz um while para que enquanto o termino da lista seja maior que 1 (Não pode haver só 1 elemento na lista) ele tornará a lista sequencial,
# enquanto o while com x maior que (termino-1) possui a condição que se o primeiro elemento da lista for maior que o segundo o valor vai mudar pra verdadeiro.

def ordenar (lista):
    nova_lista = lista
    termino= len(nova_lista)
    while termino>1:
        valor_mudado = False
        indice=0
        while indice<(termino-1):
            if nova_lista[indice] > nova_lista[indice+1]: #indice da nova lista (primeiro) for maior que indice da nova lista+1 (segundo)
                valor_mudado = True #quando mudar para verdadeiro:
                temporario = nova_lista[indice]  #cria uma variável temporária que guarda o valor da primeira posição da lista ou do primeiro valor checado
                nova_lista[indice] = nova_lista[indice+1] # O primeiro valor pega o elemento do segundo e ele troca com o primeiro lugar
                nova_lista[indice+1] = temporario
            indice=indice+1 #O indice funciona como um contador, percorrendo a lista pelos seus elemntos,
        if not valor_mudado: # e, caso a mudança de valor não ocorra.
         break
        termino = termino-1 #não pode ser o ultimo elemento da lista
    return nova_lista #retorna a lista com ordem sequencial

#Fiz uma função com parâmetro item para imprimir e coloquei a função imprimir dentro com o texto "ordenada" e a variável lista_alfanumerico.

def imprimir(item_para_imprimir):
 print("Ordenada: ", item_para_imprimir)

#Ambas as funções estão sendo chamadas no final do código principal.

