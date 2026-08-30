def main():
    inicio, fim = [int(valor) for valor in input().split()]
    horas = 0

    subtrair = 1 if inicio > fim else 0

    if inicio == fim:
        print("O JOGO DUROU 24 HORA(S)")
        return

    while inicio != fim:
        inicio += 1
        horas += 1

        if inicio > 24:
            inicio = 0

    print(f"O JOGO DUROU {horas-subtrair} HORA(S)")

if __name__ == "__main__":
    main()
