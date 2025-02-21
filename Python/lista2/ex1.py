# 1. Solicite  ao  usuário  que  insira  um  número.  
# Se o nunúmero  for  positivo,  exiba  "Número  positivo". 
# Se for negativo, exiba "Número negativo". Se for zero, exiba "Zero".

num = float(input("Insira um número: "))
if num == 0:
    print("Zero")
elif num > 0:
    print("Positivo")
else:
    print("Negativo")