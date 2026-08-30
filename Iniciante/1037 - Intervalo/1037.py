valor = float(input())

intervalo1 = lambda x: x >= 0 and x <= 25
intervalo2 = lambda x: x > 25 and x <= 50
intervalo3 = lambda x: x > 50 and x <= 75
intervalo4 = lambda x: x > 75 and x <= 100

if intervalo1(valor):
    print("Intervalo [0,25]")
elif intervalo2(valor):
    print("Intervalo (25,50]")
elif intervalo3(valor):
    print("Intervalo (50,75]")
elif intervalo4(valor):
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")
