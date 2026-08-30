segundos = int(input())
horas = minutos = 0

while segundos >= 60:
    segundos -= 60

    minutos += 1
    if minutos >= 60:
        minutos = 0
        horas += 1

print(f"{horas}:{minutos}:{segundos}")
