qntd_valores = int(input())
dentro = 0

for i in range(qntd_valores):
    num = int(input())

    if 10 <= num <= 20:
        dentro += 1

print(f"{dentro} in")
print(f"{qntd_valores-dentro} out")