# 15. Gere os 20 primeiros números da sequência de Fibonacci.

a, b = 0, 1
for i in range(20):
    print(a)
    a, b = b, a + b