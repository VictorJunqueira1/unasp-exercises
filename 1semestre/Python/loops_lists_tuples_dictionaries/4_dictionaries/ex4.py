# 4. Dado um dicionário com o nome e idade de várias pessoas, exiba apenas os maiores de idade.

pessoas = {
    "Eduardo": 20,
    "Victor": 18,
    "Emily": 16,
    "Joel": 30,
    "Esdras": 15
}

maiores_de_idade = {}
for nome, idade in pessoas.items():
    if idade >= 18:
        maiores_de_idade[nome] = idade

print("Pessoas maiores de idade:")
print(maiores_de_idade)