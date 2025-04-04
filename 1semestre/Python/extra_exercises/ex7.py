# 7. Solicite apenas 1 nome e 1 sobrenome do usuário e mostre: "Olá, Sr(a) (sobrenome)"
complete_name = input("Digite seu nome completo: ").strip().split(" ")
print(f"Olá, Sr(a) {complete_name[1].capitalize()}")