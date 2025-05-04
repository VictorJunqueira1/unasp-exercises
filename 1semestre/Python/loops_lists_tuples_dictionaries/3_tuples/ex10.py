# 10. Dada uma tupla com nomes, exiba todos os nomes que começam com a letra "A".

nomes = ("Eduardo", "Victor", "Joel", "Esdras", "Emily", "Abigail")
encontrado = False

for nome in nomes:
    if nome.startswith("A"):
        print(f"Nome: {nome}")
        encontrado = True

if not encontrado:
    print("Não encontrei nenhum nome que comece com 'A'.")