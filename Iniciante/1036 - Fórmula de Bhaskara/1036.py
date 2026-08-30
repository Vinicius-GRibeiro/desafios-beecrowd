from math import sqrt

a, b, c = [float(valor) for valor in input().split()]

delta = (b*b) - (4 * a * c)
if (a == 0) or delta < 0:
    print("Impossivel calcular")
else:
    r1 = ((0-b) + sqrt(delta)) / (2*a)
    r2 = ((0-b) - sqrt(delta)) / (2*a)

    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")