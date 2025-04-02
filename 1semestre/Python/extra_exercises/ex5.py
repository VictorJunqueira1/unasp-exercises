# 5. Usuário digite uma senha, se a senha < 8 digitos mostar:
# senha inválida. Mas se senha >= 8 digitos mostre:
# senha válida. Fazer uma criptografia
# substituindo as vogais "aeiou" por "!@#$%"

password = input("Insira uma senha: ").lower()

if len(password) < 8:
    print("Senha inválida")
else:
    password = password.replace("a", "!") \
    .replace("e", "@") \
    .replace("i", "#") \
    .replace("o", "$") \
    .replace("u", "%") 
    print("Senha validada")
    print(password)