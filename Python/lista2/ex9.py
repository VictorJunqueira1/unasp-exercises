# 9. Peça ao usuário para inserir um número. 
# Se o número estiver entre 10 e 20 (inclusive), exiba "Número entre 10 e 20", 
# caso contrário, exiba "Número fora do intervalo".

num = float(input("Insira um número: "))
if num >= 10 and num <= 20:
    print("Número entre 10 e 20")
else: 
    print("Número fora do intervalo")