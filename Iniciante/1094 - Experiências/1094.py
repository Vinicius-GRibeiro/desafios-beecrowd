cobaias = {
    "C": 0,
    "R": 0,
    "S": 0
}

n = int(input())
for i in range(n):
    lido = input().replace(" ", "")
    cobaia = lido[-1]
    qntd = int(lido[0:len(lido)-1])

    cobaias[cobaia] += qntd

total = cobaias["C"] + cobaias["R"] + cobaias["S"]
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {cobaias['C']}")
print(f"Total de ratos: {cobaias['R']}")
print(f"Total de sapos: {cobaias['S']}")

print(f"Percentual de coelhos: {(100*cobaias['C'])/total:.2f} %")
print(f"Percentual de ratos: {(100*cobaias['R'])/total:.2f} %")
print(f"Percentual de sapos: {(100*cobaias['S'])/total:.2f} %")