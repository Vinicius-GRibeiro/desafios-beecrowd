def main():
    ddd = input()

    discagem = {
        "61": "Brasilia",
        "71": "Salvador",
        "11": "Sao Paulo",
        "21": "Rio de Janeiro",
        "32": "Juiz de Fora",
        "19": "Campinas",
        "27": "Vitoria",
        "31": "Belo Horizonte",
    }

    if ddd not in discagem:
        print("DDD nao cadastrado")
        return

    print(discagem[ddd])

if __name__ == "__main__":
    main()