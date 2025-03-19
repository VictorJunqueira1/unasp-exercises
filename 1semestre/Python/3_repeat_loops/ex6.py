# Dada uma matriz 3x3 que represente o resultado de um jogo da velha,
# mostre uma mensagem com o estado atual do jogo.
# Usando as letras maiúsculas X e O, por exemplo:
# [0, 0, 1],
# [0, 1, 2],
# [2, 1, 0]
#
# O programa deve mostrar a mensagem:
# a. “Jogo ainda não acabou”, quando ainda existem espaços vazios,
# b. “X ganhou” ou “O ganhou”
# c. “Jogo empatado” quando houver um empate, óbivo.

# Matriz representando o jogo da velha
matrix = [
    [0, 0, 1],
    [0, 1, 2],
    [2, 1, 0]
]

# Mostrar a matriz do jogo substituindo os números pelos símbolos corretos
for i in range(3):
    for j in range(3):
        if matrix[i][j] == 1:
            print("X", end=" ")
        elif matrix[i][j] == 2:
            print("O", end=" ")
        else:
            print("-", end=" ")
    print()

# Verificar se alguém ganhou (linhas)
winner = 0

# Verificar se alguém ganhou (colunas)

# Verificar se alguém ganhou (diagonais)

# Verificar se ainda há espaços vazios
have_space = False

# Determinar o resultado do jogo
if winner == 1:
    print("X ganhou")
elif winner == 2:
    print("O ganhou")
elif have_space:
    print("Jogo ainda não acabou")
else:
    print("Jogo empatado")