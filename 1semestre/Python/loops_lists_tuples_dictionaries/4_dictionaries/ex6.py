# 6. Crie um dicionário com países e capitais. Deixe o usuário digitar o país e exiba a capital.

paises = {
    "Brasil": "Brasilia",
    "Estados Unidos": "Washington",
    "Chile": "Santiago",
    "Argentina": "Buenos Aires",
    "Holanda": "Amsterdam"
}

pais = input("Insira um país: ").capitalize()
print(paises.get(pais, "País nao encontrado"))