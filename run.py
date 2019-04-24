import random

populacao = list()

#Gera cromossomos da familia
for x in range(20):
    cidades = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19];
    cromossomo = list()
    for y in range(20):
        i = random.choice(cidades)
        cromossomo.append(i)
        cidades.remove(i)
    populacao.append(cromossomo)

#Gera custo
for x in range(20):


print(populacao);