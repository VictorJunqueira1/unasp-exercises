# 4. Numa fábrica, uma impressora imprime etiquetas
# para caixas. Para um tipo de caixa a impressora tem
# que usar cores que, por uma questão de
# simplicidade, são nomeadas com letras de a até m.
# As cores utilizadas pela impressora são registradas
# em uma sequência de controle. Por exemplo, uma
# string de controle "boa"
# significaria aaabbbbhaijjjm que a impressora usou
# três vezes a cor a, quatro vezes a cor b, uma vez a cor
# h e uma vez a cor a, e assim, sucessivamente. Às
# vezes há problemas: falta de cores, mau
# funcionamento técnico e uma sequência de controle
# "ruim" é produzida, por
# exemplo, aaaxbbbbyyhwawiwjjjwwm com letras
# que não são de a to m. Você tem que escrever um
# algoritmo que dada uma string, mostrará a taxa de
# erro da impressora como uma string representando
# um racional cujo numerador é o número de erros e o
# denominador o comprimento da string de controle.
# Não reduza esta fração a uma expressão mais
# simples. A string tem comprimento maior ou igual a 
# um e contém apenas letras de a até z.

string = input("Insira a string de controle: ")

num_errors = 0
for char in string:
    if char < 'a' or char > 'm':
        num_errors += 1

print(f"Taxa de erro: {num_errors}/{len(string)}")