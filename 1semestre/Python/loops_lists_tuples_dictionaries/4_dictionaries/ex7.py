# 7. Altere a idade de uma pessoa em um dicionário a partir de uma entrada do usuário.

pessoa = {
    "nome": "Eduardo",
    "idade": 21,
    "cidade": "Salvador"
}

print(f"Idade atual de {pessoa['nome']}: {pessoa['idade']}")
nova_idade = int(input(f"Insira a nova idade de {pessoa['nome']}: "))
pessoa["idade"] = nova_idade

print(pessoa)