salario = float(input())

cond15 = lambda salario: salario <= 400
cond12 = lambda salario: salario >= 400.01 and salario <= 800
cond10 = lambda salario: salario >= 800.01 and salario <= 1200
cond7 = lambda salario: salario >= 1200.01 and salario <= 2000

percentual = .15 if cond15(salario) else .12 if cond12(salario) else .1 if cond10(salario) else .07 if cond7(salario) else .04

valor_reajuste = percentual * salario
novo_salario = salario + valor_reajuste

print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {valor_reajuste:.2f}")
print(f"Em percentual: {percentual*100:.0f} %")