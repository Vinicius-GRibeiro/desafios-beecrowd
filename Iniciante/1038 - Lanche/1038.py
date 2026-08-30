cod, qntd = [int(valor) for valor in input().split()]

cardapio = {
    1: 4.0,
    2: 4.5,
    3: 5.0,
    4: 2.0,
    5: 1.5
}

total = qntd * cardapio[cod]
print(f"Total: R$ {total:.2f}")