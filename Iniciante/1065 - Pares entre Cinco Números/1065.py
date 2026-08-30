qntd_pares = 0

for i in range(5):
    num = int(input())
    if num % 2 == 0:
        qntd_pares += 1

print(f"{qntd_pares} valores pares")