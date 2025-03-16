# 5. Crie três variáveis lado1, lado2 e lado3 representando os lados de um triângulo. 
# Verifique se é um triângulo equilátero (todos os lados iguais), 
# isósceles (dois lados iguais) ou escaleno (todos os lados diferentes).

# Verificar existência do triângulo: (a + b > c) e (a + c > b) e (b + c > a)

side1 = 10
side2 = 15
side3 = 5

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    if side1 == side2 == side3:
        print("Equilátero")
    elif (side1 == side2 and side1 != side3) or (side1 == side3 and side1 != side2) or (side2 == side3 and side2 != side1):
        print("Isóceles")
    else:
        print("Escaleno")
else:
    print("Os lados não formam um triângulo")