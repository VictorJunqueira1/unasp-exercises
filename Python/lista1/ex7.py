# 7. Solicite a altura e o peso do usuário. Calcule o IMC (Índice de Massa Corporal) e imprima o resultado
height = float(input("Insira sua altura (em metros): ").replace(",", "."))
weight = float(input("Insira seu peso: ").replace(",", "."))
imc = weight / (height ** 2)
print(f"Seu IMC é: {imc:.2f}")