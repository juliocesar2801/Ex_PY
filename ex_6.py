#Exercicio 6
#crie um algoritimo para perguntar para o usuario qual o dia da semana , caso seja sabado , escreva dai de festa caso seja domingo pergunte sobre a condição fisica do usuario se estiver com dores de caebça , print recuperando entao prescisa descansar caso contrario se estiver com dores de cabeça print recuperando , entao presicsa descandsr caso o contrario apensa descanse caso nao seja sabado ou domingo mostre trabalhando trabalhando e trabalhando!

dia = input("Digite o dia da semana: ").lower()

if dia == "sabado":
    print("Dia de festa!")
    
elif dia == "domingo":
    condicao = input("Está com dor de cabeça? (s/n): ").lower()
    
    if condicao == "s":
        print("Recuperando, então precisa descansar.")
    else:
        print("Apenas descanse.")
        
else:
    print("Trabalhando, trabalhando e trabalhando!")