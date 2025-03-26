# 1. Faça um algoritmo que receba um número inteiro, 
# representando uma quantidade em segundos e exiba um texto 
# informando o total de dias, horas, minutos e segundos, quando houver um destes

segundos = int(input("Digite a quantidade de segundos: "))

dias = segundos // 86400
segundos %= 86400
horas = segundos // 3600
segundos %= 3600
minutos = segundos // 60
segundos %= 60

partes = []

if dias > 0:
    partes.append(f"{dias} dia{'s' if dias > 1 else ''}")
if horas > 0:
    partes.append(f"{horas} hora{'s' if horas > 1 else ''}")
if minutos > 0:
    partes.append(f"{minutos} minuto{'s' if minutos > 1 else ''}")
if segundos > 0 or not partes:
    partes.append(f"{segundos} segundo{'s' if segundos > 1 else ''}")

resultado = ""

for i in range(len(partes)):
    if i == len(partes) - 1:
        resultado += partes[i]
    elif i == len(partes) - 2:
        resultado += partes[i] + " e "
    else:
        resultado += partes[i] + ", "

print(resultado)