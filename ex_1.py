#Exercicio 1
#Sitema de logun com nivel de acesso. solicite usuario e senha 
#se usuario e igual a admin, crie uma estrutura de condição aninhada para solicitar senha e se a mesma for "1234", mostre que o usuario tera acesso total. caso o usuario insinra a senha incorreta, mostre senha incorreta. caso o usuario insira o usuario incorreto, mostre usuario incoreto

usuario = str(input("Digite o nome do Usuario: "))

if usuario == "admin":
    senha = float(input("Digite sua senha"))

    if senha == 1234:
        print("Sua senha esta correta acesso liberado")
    else:
        print("Sua senha esta Incorreta!")
else:
    print("seu usuario esta incorreto")









