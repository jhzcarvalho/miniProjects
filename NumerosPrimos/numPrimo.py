import math

primos_conhecidos = [2]

print("o numero 2 é primo")

for n in range(3, 100001, 2):
    ehprimo = True
    if n > 1:
        for i in primos_conhecidos:
            if i > math.sqrt(n):
                break
            if (n % i) == 0:
                ehprimo = False
                break
        if ehprimo:
            print(f"o numero {n} é primo")
            primos_conhecidos.append(n)

        else:
            print(f"O numero {n} não é primo")