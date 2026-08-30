qntd = int(input())

for i in range(qntd):
    num = int(input())

    if num == 0:
        print("NULL")
        continue

    msg = "EVEN " if num % 2 == 0 else "ODD "
    print(msg, end='')

    msg = "POSITIVE" if num > 0 else "NEGATIVE"
    print(msg)

