# 12. Crie um programa que simula o jogo Pedra, Papel e Tesoura.
# Receba a escolha do usuário e compare com uma escolha aleatória do computador.
import random

user_choice = input("Escolha Pedra, Papel ou Tesoura: ").capitalize()
computer_choice = random.choice(["Pedra", "Papel", "Tesoura"])

print(f"Usuário escolheu: {user_choice}")
print(f"Computador escolheu: {computer_choice}")

if user_choice == computer_choice:
    print("Empate!")
elif (user_choice == "Pedra" and computer_choice == "Tesoura") or \
     (user_choice == "Papel" and computer_choice == "Pedra") or \
     (user_choice == "Tesoura" and computer_choice == "Papel"):
    print("Usuário ganhou!")
else:
    print("Computador ganhou!")