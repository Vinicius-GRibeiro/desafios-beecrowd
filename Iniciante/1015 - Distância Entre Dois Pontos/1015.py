from math import sqrt, pow

x1, y1 = [float(value) for value in input().split()]
x2, y2 = [float(value) for value in input().split()]

distancia = sqrt(pow((x2-x1), 2) + pow((y2-y1), 2))

print(f"{distancia:.4f}")