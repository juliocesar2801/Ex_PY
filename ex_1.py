#Exercicio 1
#Sitema de logun com nivel de acesso. solicite usuario e senha 
#se usuario e igual a admin, crie uma estrutura de condição aninhada para solicitar senha e se a mesma for "1234", mostre que o usuario tera acesso total. caso o usuario insinra a senha incorreta, mostre senha incorreta. caso o usuario insira o usuario incorreto, mostre usuario incoreto

usuario = input("Digite o usuário: ")

if usuario == "admin":
    senha = input("Digite a senha: ")
    
    if senha == "1234":
        print("Acesso total liberado!")
    else:
        print("Senha incorreta!")
else:
    print("Usuário incorreto!")



#Exercicio 2
#calssificaão de idade . solicite idade, se idade for Maior ou igual a 18 , crie uma estrutuara de condiçoes aninhada para vereficar se a idade e maior ou igual a 60 se for mostre que e idoso , senao , mostre que e adulto, se idade for maior igual 60 , se for , moestre que e idoso , senao mostre q e um adulto , se a idade for maior ou igual a 12, adolecente , caso contrario criança


idade = int(input("Digite sua idade: "))

if idade >= 18:
    if idade >= 60:
        print("Idoso")
    else:
        print("Adulto")
elif idade >= 12:
    print("Adolescente")
else:
    print("Criança")



#Exercicio 3
#Aprovação com distinção . solicite nota , se nota for maior ou igual a 6 crie condiçã de aninhamento para verficar se a nora e maior ou igual a 9 se for aprovada com ecelencia se a nota for maior ou igual a 9 aprovada . caso contrario reprovada


nota = float(input("Digite sua nota: "))

if nota >= 6:
    if nota >= 9:
        print("Aprovado com excelência!")
    else:
        print("Aprovado!")
else:
    print("Reprovado!")


#Exercicio 4
#verificação de numero solicite o numero e verefique se ele e maior que 0 se for crie uma estrtura de condição aninhada para verificar se este numero e par se for print positivvo e par , se nao for positivo e impar . se numero for iguak a zero print zero caso o contrario negativo


numero = int(input("Digite um número: "))

if numero > 0:
    if numero % 2 == 0:
        print("Positivo e par")
    else:
        print("Positivo e ímpar")
elif numero == 0:
    print("Zero")
else:
    print("Negativo")


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