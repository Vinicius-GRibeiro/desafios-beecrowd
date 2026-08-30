a, b, c = [int(val) for val in input().split()]

maiorAB = (a+b+abs(a-b)) / 2
maiorABC = int((maiorAB + c + abs(maiorAB - c)) / 2)

print(f"{maiorABC} eh o maior")