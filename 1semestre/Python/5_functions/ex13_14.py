# 13. Implemente uma função que receba uma frase e
# transforme-a em uma string criptografada. A string
# criptografada deve conter cada caractere presente na
# frase, seguido por suas posições na string original. Cada
# caractere deve ser seguido pelo símbolo = e suas posições
# separadas por &. Diferentes caracteres devem ser
# separados por #. A frase só deve conter letras maiúsculas
# ou minúsculas e números e espaços.
# Entrada:
# A casa caiu
# Saída Esperada:
# A=0# =1&3&7#a=2&4&6&8#c=5#s=9#i=10&11#u=12

def criptografar(frase):
    mapa = {}
    
    for i, char in enumerate(frase):
        if char not in mapa:
            mapa[char] = []
        mapa[char].append(str(i))
    
    partes = []
    for char, posicoes in mapa.items():
        partes.append(f"{char}=" + "&".join(posicoes))
    
    return "#".join(partes)

# 14. Baseado na questão anterior, implemente uma função
# que descriptografe a string. Ou seja:
# Entrada esperada:
# A=0# =1&3&7#a=2&4&6&8#c=5#s=9#i=10&11#u=12
# Saída esperada:
# A casa caiu

def descriptografar(string):
    partes = string.split("#")

    posicoes = []
    for parte in partes:
        char, indices = parte.split("=")
        for indice in indices.split("&"):
            posicoes.append((int(indice), char))

    posicoes.sort()

    tamanho = posicoes[-1][0] + 1
    frase = [""] * tamanho

    for pos, char in posicoes:
        frase[pos] = char

    return "".join(frase)

frase_original = "A casa caiu"
criptografada = criptografar(frase_original)
descriptografada = descriptografar(criptografada)

print("Frase original:", frase_original)
print("Criptografada:", criptografada)
print("Descriptografada:", descriptografada)