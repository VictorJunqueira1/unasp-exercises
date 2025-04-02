# 1. Solicite nome completo
# se o nome tiver mais de 10 letras
# imprimir "seu nome é muito grande"
# caso contrário, "seu nome é pequeno"

name = input("Insira seu nome completo: ")
if len(name) > 10:
    print("Seu nome é muito grande")
else:
    print("Seu nome é pequeno")