valor = int(input())
valor_aux = valor
notas = {
    100: 0,
    50: 0,
    20: 0,
    10: 0,
    5: 0,
    2: 0,
    1: 0
}

for nota in notas:
    while valor_aux >= nota:
        divisao_inteira = valor_aux // nota
        notas[nota] += divisao_inteira
        valor_aux = valor_aux - (divisao_inteira * nota)

print(valor)
for nota, quantidade in notas.items():
    print(f"{quantidade} nota(s) de R$ {nota},00")
