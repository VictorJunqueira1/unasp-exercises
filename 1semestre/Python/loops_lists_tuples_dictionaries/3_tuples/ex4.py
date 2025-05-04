# 4. Leia 3 nomes e armazene-os em uma tupla. Verifique se um nome específico está na tupla.

nomes = tuple(input("Insira um nome: ") for _ in range(3))
nome_procurado = input("Insira o nome que deseja procurar: ")

print(f"O nome {nome_procurado} {'está' if nome_procurado in nomes else 'não está'} na tupla.")