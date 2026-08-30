a, b, c, d = [int(valor) for valor in input().split()]

condicoes = [b > c, d > a, c+d > a+b, c > 0, d > 0, a % 2 == 0]

if all(condicoes):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
