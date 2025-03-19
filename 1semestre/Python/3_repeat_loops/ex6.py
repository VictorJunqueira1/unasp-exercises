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
for i in range(3):
    if matrix[i][0] == matrix[i][1] == matrix[i][2] and matrix[i][0] != 0:
        winner = matrix[i][0]

# Verificar se alguém ganhou (colunas)
for i in range(3):
    if matrix[0][i] == matrix[1][i] == matrix[2][i] and matrix[0][i] != 0:
        winner = matrix[0][i]

# Verificar se alguém ganhou (diagonais)
if matrix[0][0] == matrix[1][1] == matrix[2][2] and matrix[0][0] != 0:
    winner = matrix[0][0]

if matrix[0][2] == matrix[1][1] == matrix[2][0] and matrix[0][2] != 0:
    winner = matrix[0][2]

# Verificar se ainda há espaços vazios
have_space = False
for i in range(3):
    for j in range(3):
        if matrix[i][j] == 0:
            have_space = True

# Determinar o resultado do jogo
if winner == 1:
    print("X ganhou")
elif winner == 2:
    print("O ganhou")
elif have_space:
    print("Jogo ainda não acabou")
else:
    print("Jogo empatado")