def main():
    valores = [float(valor) for valor in input().split()]
    valores.sort(reverse=True)

    is_not_triangulo = lambda a, b, c: a >= b + c
    is_retangulo = lambda a, b, c: (a*a) == (b*b) + (c*c)
    is_obtusangulo = lambda a, b, c: (a*a) > (b*b) + (c*c)
    is_acutangulo = lambda a, b, c: (a*a) < (b*b) + (c*c)
    is_equilatero = lambda a, b, c: a == b == c
    is_isosceles = lambda a, b, c: (a==b and c!=a) or (a==c and b!=a) or (c==b and a!=c)

    triangulos = {
        is_not_triangulo: "NAO FORMA TRIANGULO",
        is_retangulo: "TRIANGULO RETANGULO",
        is_obtusangulo: "TRIANGULO OBTUSANGULO",
        is_acutangulo: "TRIANGULO ACUTANGULO",
        is_equilatero: "TRIANGULO EQUILATERO",
        is_isosceles: "TRIANGULO ISOSCELES"
    }

    for func, msg in triangulos.items():
        if func(*valores):
            print(msg)
            if msg == "NAO FORMA TRIANGULO":
                return


if __name__ == "__main__":
    main()
