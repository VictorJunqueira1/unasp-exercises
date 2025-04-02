# 5. Jaden Smith, filho de Will Smith, é estrela de filmes
# como The Karate Kid (2010) e After Earth (2013). 
# Jaden também é conhecido por algumas de suas
# filosofias que transmite via Twitter. Ao escrever no
# Twitter, ele é conhecido por quase sempre colocar
# cada palavra em maiúscula. Para simplificar, você
# terá que colocar cada palavra em maiúscula, veja
# como são esperadas as contrações no exemplo
# abaixo. Sua tarefa é fazer um algoritmo que dada uma
# entrada de texto, convertê-las para como seriam
# escritas por Jaden Smith.

text = input("Insira o texto: ")
words = text.split()
jaden_words = [word.capitalize() for word in words]
print(" ".join(jaden_words))