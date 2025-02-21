# 8. Crie uma variável ano e atribua um valor numérico. 
# Verifique se o ano é bissexto.  
# Se for, exiba "Ano bissexto", caso contrário, exiba "Ano não bissexto"

year = int(input("Insira o ano: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("Ano bissexto")
else:
    print("Ano não bissexto")