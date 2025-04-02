# 1. Faça um algoritmo que receba um número inteiro, 
# representando uma quantidade em segundos e exiba um texto 
# informando o total de dias, horas, minutos e segundos, quando houver um destes

seconds = int(input("Digite a quantidade de seconds: "))

days = seconds // 86400
seconds %= 86400
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60

parts = []

if days > 0:
    parts.append(f"{days} dia{'s' if days > 1 else ''}")
if hours > 0:
    parts.append(f"{hours} hora{'s' if hours > 1 else ''}")
if minutes > 0:
    parts.append(f"{minutes} minuto{'s' if minutes > 1 else ''}")
if seconds > 0 or not parts:
    parts.append(f"{seconds} segundo{'s' if seconds > 1 else ''}")

resultado = ""

for i in range(len(parts)):
    if i == len(parts) - 1:
        resultado += parts[i]
    elif i == len(parts) - 2:
        resultado += parts[i] + " e "
    else:
        resultado += parts[i] + ", "

print(resultado)