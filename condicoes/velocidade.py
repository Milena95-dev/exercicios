#escrever um script que pergunte a velocidade do carro
#caso ultrapasse 80km/h mostrar a mensagem dizendo: voce foi multado, se multado, exibir o valor da multa

velocidade_registrada = int(input("digite a velocidade"))
velocidade_padrao = 80
multa = (velocidade_registrada - velocidade_padrao)*5

if velocidade_registrada<=velocidade_padrao:
    print("esta tudo certo, voce nao sera multado")
else:
    print("voce esta acima da velocidade permitida, portanto sua multa sera de %4.2f"%multa)

