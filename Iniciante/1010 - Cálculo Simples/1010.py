cod_p1, qntd_p1, val_p1 = [int(val) if '.' not in val else float(val) for val in input().split()]
cod_p2, qntd_p2, val_p2 = [int(val) if '.' not in val else float(val) for val in input().split()]

total = (qntd_p1 * val_p1) + (qntd_p2 * val_p2)
print(f"VALOR A PAGAR: R$ {total:.2f}")