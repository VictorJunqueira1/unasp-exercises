# 9. Crie um jogo de adivinhação: o computador escolhe um número de 1 a 100 e o usuário tenta adivinhar.
import random

secret_number = random.randint(1, 100)
attempts = 0

while attempts != secret_number:
    attempts = int(input("Adivinhe o número (entre 1 e 100): "))
    if attempts < secret_number:
        print("Mais baixo!")
    elif attempts > secret_number:
        print("Mais alto!")
    else:
        print("Acertou!")