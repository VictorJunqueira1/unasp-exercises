# 12. Peça uma senha ao usuário até que ele digite a senha correta.

senha_correta = "1234"
while True:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Acesso permitido.")
        break
    else:
        print("Senha incorreta.")