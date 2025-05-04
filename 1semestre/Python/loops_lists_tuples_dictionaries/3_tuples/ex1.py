# 1. Crie uma tupla com os 7 dias da semana e permita que o usuário escolha um número de 1 a 7 para exibir o dia correspondente.

dias = ("Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado")
while True:
    opcao = int(input("Insira um número de 1 a 7 para exibir o dia correspondente: "))
    if opcao < 1 or opcao > 7:
        print("Opção inválida!")
    else:
        print(dias[opcao - 1])
        break