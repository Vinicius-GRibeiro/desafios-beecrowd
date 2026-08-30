def main():
    a, b, c = [float(valor) for valor in input().split()]

    c1 = lambda a, b, c: (a + b) > c
    c2 = lambda a, b, c: (a + c) > b
    c3 = lambda a, b, c: (b + c) > a

    if c1(a, b, c) and c2(a, b, c) and c3(a, b, c):
        perimetro = a + b + c
        print(f"Perimetro = {perimetro:.1f}")
        return

    area = (a+b) * c / 2
    print(f"Area = {area:.1f}")

if __name__ == "__main__":
    main()