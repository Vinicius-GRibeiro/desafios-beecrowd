vendedor = input()
salario_fixo = float(input())
total_vendas = float(input())

porcentagem_comissao = .15
total = salario_fixo + (total_vendas * porcentagem_comissao)
print(f"TOTAL = R$ {total:.2f}")