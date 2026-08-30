casos = int(input())

p1, p2, p3 = 2, 3, 5

for i in range(casos):
    n1, n2, n3 = [float(i) for i in input().split()]
    media = ((n1*p1) + (n2*p2) + (n3*p3)) / (p1+p2+p3)
    print(f"{media:.1f}")