# 11. Crie uma função chamada quadrado que recebe dois
# parâmetros, um para a base e outro para a altura mostre
# um quadrado feito por asteriscos.
# Por exemplo, para os valores 5 e 3 a saída de ser:
# *  *  *  *  *
# *  *  *  *  *
# *  *  *  *  *

def quadrado(base, altura):
    linha = " ".join(["*"] * base)
    for i in range(altura):
        print(linha)

quadrado(5, 3)
