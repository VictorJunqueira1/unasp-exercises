# 7. Crie uma variável mes e atribua um valor de 1 a 12 representando um mês. 
# Exiba o nome do mês correspondente (por exemplo, se mes for 1, exiba "Janeiro").

month = int(input("Insira o número do mês: "))
months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", 
         "Junho", "Julho", "Agosto", "Setembro", 
         "Outubro", "Novembro", "Dezembro"]

if month > 12 or month < 1:
    print("Mês inválido")
else:
    print(months[month - 1])