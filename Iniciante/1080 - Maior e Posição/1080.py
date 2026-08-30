maior, index = -1, 0

for i in range(100):
    n = int(input())
    if n > maior:
        maior = n
        index = i+1

print(maior)
print(index)
