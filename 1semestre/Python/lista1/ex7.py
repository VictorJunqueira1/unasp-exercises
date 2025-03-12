# 7. Solicite a altura e o peso do usuário. Calcule o IMC (Índice de Massa Corporal) e imprima o resultado
height = float(input("Insira sua altura (em metros): ").replace(",", "."))
weight = float(input("Insira seu peso: ").replace(",", "."))
imc = weight / (height ** 2)
print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidade")