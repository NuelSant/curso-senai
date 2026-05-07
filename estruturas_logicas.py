nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cnh = input("Tem CNH? (sim/não)")

if idade >= 18 and cnh == "sim":
    print("você pode dirigir👌")
else:
    print("você não pode dirigir")

#operador or
if idade <= 18 or idade >= 60:
    estudante = input("vocé é estudante?(sim/não) ")
    if estudante == "sim" or idade <= 60:
        print("você ganhou um desconto para a sua CNH!")
    else:
        print("Vaza daqui")
else: 
    print("você não pode dirigir!")
