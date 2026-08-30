n1, n2, n3, n4 = [float(valor) for valor in input().split()]
p1, p2, p3, p4 = 2, 3, 4, 1

media = ((p1 * n1) + (p2 * n2) + (p3 * n3) + (p4 * n4)) / (p1 + p2 + p3 + p4)

print(f"Media: {media:.1f}")

if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exame = float(input())
    media = (media + exame) / 2
    print(f"Nota do exame: {exame:.1f}")
    if media >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    print(f"Media final: {media:.1f}")