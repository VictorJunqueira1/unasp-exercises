# 11. Implemente um programa que solicita ao usuário 
# o ano de nascimento e classifica a faixa etária em
# "Criança", "Adolescente", "Adulto Jovem" ou "Adulto".

birth_year = int(input("Insira o ano de nascimento: "))
current_year = 2025
age = current_year - birth_year

if age <= 12:
    print(f"Criança ({age} anos).")
elif age <= 17:
    print(f"Adolescente ({age} anos).")
elif age <= 25:
    print(f"Adulto Jovem ({age} anos).")
else:
    print(f"Adulto ({age} anos).")