# 7. Crie uma função chamada "calcular_desconto" que
# recebe o valor de um produto e uma porcentagem de
# desconto como argumentos, e retorna o valor do produto
# com o desconto aplicado.

def calcular_desconto(preco, desconto):
    valor_do_desconto = preco * (desconto / 100)
    return preco - valor_do_desconto

print(calcular_desconto(100, 10))