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