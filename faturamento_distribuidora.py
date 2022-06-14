# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
#_________________________________________________________________________________________________________________________

import json

#importando e abrindo o arquivo json
with open("dados.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)


maior = 0
menor = float('inf')
media = 0
cont = 0
dias_superior_media = 0
# para cada item do arquivo json
for i in dados:
    #Para descobrir o valor de maior faturamento e seu dia
    if i['valor'] > maior:
        maior = i['valor']
        dia_maior = i['dia']
    #Considerei que o valor 0 não é um valor de faturamento, ingnorando os dias com valor 0
    #Para descobrir o valor de menor faturamento e seu dia
    elif i['valor'] < menor and i['valor'] != 0:
        menor = i['valor']
        dia_menor = i['dia']
    #Para descobrir a media de faturamento sem considerar os dias com valor 0
    if i['valor'] != 0:
        media += i['valor']
        cont += 1
    media = media/cont
    #se valor superior a media, conta mais um dia
    if i['valor'] > media:
        dias_superior_media+= 1 


print(f'A media mensal foi de R$ {media:.2f}')   
print(f'A quantidade de dias com valor superior a media foi de {dias_superior_media}dias')
print(f'O valor maximo foi: R$ {maior:.2f} no dia {dia_maior}')
print(f'O valor minimo foi: R$ {menor:.2f} no dia {dia_menor}')

   
