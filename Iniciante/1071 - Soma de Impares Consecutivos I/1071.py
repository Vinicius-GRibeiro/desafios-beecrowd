inicio = int(input())
fim = int(input())
soma = 0

incremento = 1 if inicio < fim else -1

for i in range(inicio + incremento, fim, 1 if inicio < fim else -1):
    if i % 2 != 0:
        soma += i

print(soma)