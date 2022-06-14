# Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# SP – R$67.836,43
# RJ – R$36.678,66
# MG – R$29.229,88
# ES – R$27.165,48
# Outros – R$19.849,53
# Calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

total = (sp + rj + mg + es + outros)
print(f'O valor total da distribuidora foi: R$ {total}')

porcetagem_sp = ((sp/total)*100)
porcetagem_rj = ((rj/total)*100)
porcetagem_mg = ((mg/total)*100)
porcetagem_es = ((es/total)*100)
porcetagem_out = ((outros/total)*100)

print('Porcentagem de SP {:.2f}%'.format(porcetagem_sp))
print('Porcentagem de RJ {:.2f}%'.format(porcetagem_rj))
print('Porcentagem de MG {:.2f}%'.format(porcetagem_mg))
print('Porcentagem de ES {:.2f}%'.format(porcetagem_es))
print('Porcentagem de outros estados {:.2f}%'.format(porcetagem_out))