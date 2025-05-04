# 10. Crie um dicionário com nomes de alunos e uma lista de 3 notas. Exiba a média de cada um.

alunos = {
    "Eduardo": [4, 6, 8],
    "Victor": [10, 8, 7],
    "Joel": [8, 7, 7],
    "Esdras": [7, 8, 6],
    "Emily": [10, 10, 10]
}

for aluno, notas in alunos.items():
    media = sum(notas) / len(notas)
    print(f"A média de {aluno} é: {media:.2f}")