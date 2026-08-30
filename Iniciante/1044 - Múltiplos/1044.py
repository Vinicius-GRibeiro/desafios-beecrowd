def main():
    a, b = [int(valor) for valor in input().split()]

    dividendo = a if a > b else b
    divisor = a if a < b else b

    if dividendo % divisor == 0:
        print("Sao Multiplos")
        return

    print("Nao sao Multiplos")

if __name__ == "__main__":
    main()
