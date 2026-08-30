from datetime import datetime

inicio = [int(input().replace("Dia ", ""))]
inicio.extend([int(valor) for valor in input().strip().replace(":", " ").split()])

fim = [int(input().replace("Dia ", ""))]
fim.extend([int(valor) for valor in input().strip().replace(":", " ").split()])

inicio = datetime(1, 4, inicio[0], inicio[1], inicio[2], inicio[3], 0)
fim = datetime(1, 4, fim[0], fim[1], fim[2], fim[3], 0)

diferenca = fim - inicio
dias = diferenca.days
horas = diferenca.seconds // 3600
minutos = (diferenca.seconds % 3600) // 60
segundos = diferenca.seconds % 60

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")
