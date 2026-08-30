valores = [int(valor) for valor in input().split()]
valores_c = valores.copy()

# valores_ordenados.sort()

# Hard coded
for i in range(len(valores_c)):
    for index, valor in enumerate(valores_c):
        if index+1 > len(valores_c)-1:
            continue

        if valor > valores_c[index + 1]:
            valores_c[index] = valores_c[index+1]
            valores_c[index+1] = valor

for valor in valores_c:
    print(valor)

print()

for valor in valores:
    print(valor)
