# 7. Dado um conjunto de strings, faça um algoritmo que
# calcule o perímetro total de todas as ilhas. Cada
# pedaço de terreno será marcado com 'X' enquanto
# os campos de água são representados como 'O'.
# Considere cada peça como um 1x1 pedaço de
# terreno perfeito.

grid1 = [
    "XOOXO",
    "XOOXO",
    "OOOXO",
    "XXOXO",
    "OXOOO"
]

grid2 = [
    "XOOO",
    "XOXO",
    "XOXO",
    "OOXX",
    "OOOO"
]

grid = grid1  # Escolha a grade a ser utilizada

if grid:
    rows = len(grid)
    columns = len(grid[0])
    perimeter = 0
    
for i in range(rows):
    for j in range(columns):
        if grid[i][j] == 'X':
            sides = 4

            # Verificar lados vizinhos (acima, abaixo, esquerda e direita)
            
            if i > 0 and grid[i - 1][j] == 'X':           # Acima
                sides -= 1
            if i < rows - 1 and grid[i + 1][j] == 'X':    # Abaixo
                sides -= 1
            if j > 0 and grid[i][j - 1] == 'X':           # Esquerda
                sides -= 1
            if j < columns - 1 and grid[i][j + 1] == 'X': # Direita
                sides -= 1
            
            perimeter += sides
            
print(perimeter)