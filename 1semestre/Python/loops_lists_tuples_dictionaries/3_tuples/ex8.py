# 8. Dada uma tupla com notas, calcule a média e informe se o aluno está aprovado (média >= 6).

notas = tuple(float(input(f"Insira a {i+1}ª nota: ")) for i in range(4))
media = sum(notas) / len(notas)

print(f"A média das notas é: {media:.2f}")
print("Aluno aprovado! ✅" if media >= 6 else "Aluno reprovado! ❌")