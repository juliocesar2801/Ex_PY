#Exercicio 5
#sistema de desconto solicite valose e se a pessoa e vip ou nao if valor maior ou igual a 200 , crie uma esrutura de considção aninhada para vereficar se a pessoa e vip ,se for , ofereça 20% sobre o valor e mostre o valor de desconto e o valor final, considerando o desconto , senao for vip ofereça desconto de 10%
valor = float(input("Digite o valor da compra: "))
vip = input("É cliente VIP? (s/n): ")

if valor >= 200:
    if vip == "s":
        desconto = valor * 0.20
    else:
        desconto = valor * 0.10

    valor_final = valor - desconto

    print("Desconto:", desconto)
    print("Valor final:", valor_final)
else:
    print("Sem desconto")