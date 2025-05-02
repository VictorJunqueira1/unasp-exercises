# 9. Crie uma lista com 10 números aleatórios entre 1 e 100 e ordene-a.

import random

lista = [random.randint(1, 100) for _ in range(10)]

print(f"Lista: {lista}")

lista.sort()
print(f"Lista ordenada: {lista}")