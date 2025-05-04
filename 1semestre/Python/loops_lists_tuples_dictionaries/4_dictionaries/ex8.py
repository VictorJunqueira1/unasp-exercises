# 8. Remova um item de um dicionário com base em uma chave digitada pelo usuário.

pessoa = {
    "nome": "Eduardo",
    "idade": 21,
    "cidade": "Salvador"
}

chave = input("Insira a chave que deseja remover (nome, idade, cidade): ").lower()
if chave in pessoa:
    del pessoa[chave]
else:
    print("Chave não encontrada")

print(pessoa)