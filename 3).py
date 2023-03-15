"""
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

"""

import json

#abrindo arquivo json
with open("dados.json", encoding='utf-8') as arq_json:
    dados = json.load(arq_json)
  
lista_chaves = []
lista_valores = []

           
#adicionando chaves e valores nas listas acima
for chaves in dados:
    lista_chaves.append(chaves.get("dia"))

for valores in dados:
  lista_valores.append(valores.get("valor"))

#excluindo valores iguais a 0.0
lista_arrumada = []
for elemento in lista_valores:
    if elemento not in lista_arrumada:
        lista_arrumada.append(elemento)
  

print(" ")

print("chaves: \n", lista_chaves)
print("\nValores: \n", lista_arrumada)

#excluindo o ultimo valor 0.0
indice = lista_arrumada.index(0.0)
del lista_arrumada[indice]

print()

#Questões
print("Menor valor de faturamento: ", min(lista_arrumada))
print("Maior valor de faturamento: ", max(lista_arrumada))

media_mensal = sum(lista_arrumada) / len(lista_arrumada)
print("Media mensal: {:.4f}".format(media_mensal)) 
