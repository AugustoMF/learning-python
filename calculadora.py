num1 = int(input("Insira um número: "))
num2 = int(input("Insira o segundo número: "))

print (""""
Para somar, digite (A)
Para subtrair, digite (S)
Para multiplicar, digite (M)
Para dividir, digite (D)
""")

tipoOperacao = input("Insira o tipo de operação que deseja efetuar: ")

if tipoOperacao.lower() == "a":
    print (num1 + num2)
elif tipoOperacao.lower() == "s":
    print (num1 - num2)
elif tipoOperacao.lower() == "m":
    print (num1 * num2)
elif tipoOperacao.lower() == "d":
    print (num1 / num2)
else:
    print ("Operação inválida!")
