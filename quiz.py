print("Bem-vindo ao meu quiz de NASCAR")

playing = input("Você quer jogar? ")
if playing.lower() != "sim":
    quit()

print("Então vamos começar!")

busch = input("Quantas vitórias Kyle Busch tem na NASCAR Cup Series? (Digite em números) ")
if busch == "63":
    print("Acertou!")
else:
    print("Errou, tente novamente")
    quit()

maiorVencedor = input("Qual é o piloto com mais vitórias na NASCAR Cup Series? ")
if maiorVencedor.lower() == "richard petty":
    print("Parabéns, mais um acerto")
else:
    print("Errou, volte para o começo!")
    quit()

print("Vamos dificultar um pouco mais!")

campeão = input("Quem foi o primeiro campeão da categoria? ")
if campeão.lower() == "red byron":
    print("Mais um acerto! Você entende bastante.")
else:
    print("Errado, volte ao começo")
    quit()

quant = input("Quantas categorias tem a NASCAR a nível nacional? (Digite em números) ")
if quant == "3":
    print("Parabéns, mais um acerto!")
else:
    print("Errado, volte ao começo")
    quit()

firstRace = input ("Quem venceu a primeira corrida da história da cup? ")
if firstRace.lower() == "red byron":
    print("Mais um acerto, siga em frente!")
else: 
    print ("Errado, volte ao começo")
    quit()

charlotte = input("Quando foi realizado a primeira Coca-Cola 600 (Digite em números) ")
if charlotte == "1960":
    print("Acertou!")
else:
    print("Errou, tente novamente")
    quit()

newHampshire = input("Em que ano a última corrida do ano foi realizada em New Hampshire? (Digite em números) ")
if newHampshire == "2001":
    print("Acertou!")
else:
    print("Errou, tente novamente")
    quit()

numero = input ("Qual o número com mais vitórias na NASCAR? ")
if numero == "11":
    print ("Outro acerto")
else: 
    print("Errou, tente novamente")
    quit()

corridaLonga = input("Qual a corrida mais longa da história realizada em um unico dia? ")
if corridaLonga.lower() == "coca cola 600 de 2020":
    print("Correto")
else:
    print("Errado, volte ao começo")
    quit()

pilotoRico = input("Quem é o piloto mais rico da história da categoria? ")
if pilotoRico.lower() == "dale earnhardt jr":
    print("Correto")
else:
    print("Errado, volte ao começo")
    quit()

print ("Prabéns, você chegou ao fim do meu quiz de NASCAR!")
