def main():
    hora_inicio, minuto_inicio, hora_fim, minuto_fim = [int(valor) for valor in input().split()]
    inicio = hora_inicio * 60 + minuto_inicio
    fim = hora_fim * 60 + minuto_fim

    if fim <= inicio:
        fim += 24 * 60

    duracao = fim - inicio

    horas = duracao // 60
    minutos = duracao % 60

    print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")

if __name__ == "__main__":
    main()
