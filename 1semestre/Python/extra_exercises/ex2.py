# 2. Receber string do usuário e entregar ela invertida
# e mostre na tela quantas vogais tem esse texto
name = input("Insira uma frase: ")
print(name[::-1])
vowels = ["a", "e", "i", "o", "u"]
count = 0

for char in name:
    if char in vowels:
        count += 1

print(count)