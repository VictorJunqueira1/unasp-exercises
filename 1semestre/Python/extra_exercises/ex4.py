# 4. Dado uma variavel, cujo tenha que ser "complete_name" e *sempre 3 palavras*, 
# mostre as iniciais em letras maiúsculas

complete_name = input("Insira seu nome completo: ").strip()
if complete_name.count(" ") == 2:
    name = complete_name.split()
    print(f"{name[0][0].upper()}-{name[1][0].upper()}-{name[2][0].upper()}")
elif complete_name.count(" ") > 2:
    print("Insira um nome até 3 palavras")
else:
    print("Insira um nome completo, maior que 3 palavras")