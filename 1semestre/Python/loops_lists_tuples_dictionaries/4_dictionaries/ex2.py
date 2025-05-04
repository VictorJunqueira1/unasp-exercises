# 2. Crie um dicionário com 5 alunos e suas notas. Depois, exiba a média geral da turma.

alunos = {
    "Eduardo": 10,
    "Victor": 9,
    "Joel": 8,
    "Esdras": 7,
    "Emily": 6
}

media = sum(alunos.values()) / len(alunos)
print(f"A média geral da turma é: {media:.2f}")