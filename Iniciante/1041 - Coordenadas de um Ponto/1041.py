x, y = [float(valor) for valor in input().split()]

condicao_eixo_unico = lambda a: a == 0
condicao_origem = lambda x, y: condicao_eixo_unico(x) and condicao_eixo_unico(y)
condicao_Q1 = lambda x, y: x > 0 and y > 0
condicao_Q2 = lambda x, y: x < 0 and y > 0
condicao_Q3 = lambda x, y: x < 0 and y < 0

if condicao_origem(x, y):
    localizacao = "Origem"
elif condicao_eixo_unico(x):
    localizacao = "Eixo Y"
elif condicao_eixo_unico(y):
    localizacao = "Eixo X"
elif condicao_Q1(x, y):
    localizacao = "Q1"
elif condicao_Q2(x, y):
    localizacao = "Q2"
elif condicao_Q3(x, y):
    localizacao = "Q3"
else:
    localizacao = "Q4"

print(localizacao)