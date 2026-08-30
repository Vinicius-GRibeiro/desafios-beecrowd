soma_positivos = 0
qntd_positivos = 0

for i in range(6):
    num = float(input())

    if num > 0:
        soma_positivos += num
        qntd_positivos += 1

print(f"{qntd_positivos} valores positivos")
print(f"{soma_positivos/qntd_positivos:.1f}")