# 3. Faça um algoritmo que receba uma frase
# converta cada palavra em hashtags para redes sociais, sendo que:
# a. Deve começar com uma hashtag (#).
# b. Todas as palavras devem ter a primeira letra maiúscula.
# c. Apenas palavras a partir de 05 caracteres
# Por exemplo, se a entrada for a frase:
# a mancha verde é o poder,
# a saída deve ser: #Mancha #Verde #Poder.

phrase = input("Insira uma frase: ")
words = phrase.split()
hashtags = ["#" + word.capitalize() for word in words if len(word) >= 5]
print(" ".join(hashtags))