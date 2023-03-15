"""
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.
"""

SP = 67836.43
RJ  = 36678.66
MG = 29229.88
ES = 27165.48
Outros = 19849.53

total = SP + RJ + MG + ES + Outros

percen_Sp =  (SP/total) * 100
percen_rj = (RJ/total) * 100
percen_mg = (MG/total) * 100
percen_es = (ES/total) * 100
percen_outros = (Outros/total) * 100

print("percentual de representação de SP {:.2f}%: ".format(percen_Sp))
print("percentual de representação de RJ {:.2f}%: ".format(percen_rj))
print("percentual de representação de MG {:.2f}%: ".format(percen_mg))
print("percentual de representação de ES {:.2f}%: ".format(percen_es))
print("percentual de representação de outros estados {:.2f}%: ".format(percen_outros))


