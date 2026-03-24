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