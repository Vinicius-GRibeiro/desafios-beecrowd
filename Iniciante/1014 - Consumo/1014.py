distancia_percorrida_KM = int(input())
combustivel_gasto_L = float(input())

kml = distancia_percorrida_KM / combustivel_gasto_L
print(f"{kml:.3f} km/l")