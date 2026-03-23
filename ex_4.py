#Exercicio 4
#verificação de numero solicite o numero e verefique se ele e maior que 0 se for crie uma estrtura de condição aninhada para verificar se este numero e par se for print positivvo e par , se nao for positivo e impar . se numero for iguak a zero print zero caso o contrario negativo

numero = float(input("Digite seu numero: "))
if numero > 0:
    if numero % 2 == 0:
        print("Positivo e par")
    else:
        print("Positivo e ímpar")
elif numero == 0:
    print("Zero")
else:
    print("Negativo")