# 8. Crie uma função chamada "verificar_anagrama" que
# recebe duas strings como argumentos e retorna True se as
# strings forem anagramas (ou  seja, possuírem as mesmas
# letras, independentemente da ordem), e False caso
# contrário.

def verificar_anagrama(str1, str2):
    return sorted(str1) == sorted(str2)

print(verificar_anagrama("listen", "silent"))