# Faça um algoritmo que receba um número inteiro, 
# representando uma quantidade em segundos e exiba um texto 
# informando o total de dias, horas, minutos e segundos, quando houver um destes

def formatar_tempo(segundos: int) -> str:
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

    return ", ".join(partes[:-1]) + (" e " + partes[-1] if len(partes) > 1 else partes[0])

segundos = int(input("Digite a quantidade de segundos: "))
print(formatar_tempo(segundos))