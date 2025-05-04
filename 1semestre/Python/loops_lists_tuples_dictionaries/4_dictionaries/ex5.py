# 5. Permita ao usuário buscar uma chave no dicionário e exibir o valor correspondente.

pessoa = {
    "nome": "Eduardo",
    "idade": 21,
    "cidade": "Salvador"
}

chave = input("Insira a chave que deseja buscar (nome, idade, cidade): ")
print(pessoa.get(chave, "Chave não encontrada"))