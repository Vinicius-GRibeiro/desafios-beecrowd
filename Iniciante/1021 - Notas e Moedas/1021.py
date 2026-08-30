valor = int(float(input()) * 100)
valor_aux = valor

notas = {
    10000: 0,
    5000: 0,
    2000: 0,
    1000: 0,
    500: 0,
    200: 0,
}

moedas = {
    100: 0,
    50: 0,
    25: 0,
    10: 0,
    5: 0,
    1: 0,
}

for nota in notas:
    while valor_aux >= nota:
        divisao_inteira = valor_aux // nota
        notas[nota] += divisao_inteira
        valor_aux = valor_aux - (divisao_inteira * nota)

for moeda in moedas:
    while valor_aux >= moeda:
        divisao_inteira = valor_aux // moeda
        moedas[moeda] += divisao_inteira
        valor_aux = valor_aux - (divisao_inteira * moeda)


print("NOTAS:")
for nota, quantidade in notas.items():
    print(f"{int(quantidade)} nota(s) de R$ {nota/100:.2f}")

print("MOEDAS:")
for moeda, quantidade in moedas.items():
    print(f"{int(quantidade)} moeda(s) de R$ {moeda/100:.2f}")

