import random
import math

qtdCromossomos = 20
qtdGenes = 20
cromossomos = []

def funcaoFitness(populacao, cx, cy):
    # gera matriz 20x21 da populacao onde a ultima coluna eh a copia da primeira coluna
    tour = [x + [x[0]] for x in populacao]

    # inicializa matriz de 20x20 com valor 0 em todas as posições
    dcidade = [[0 for x in range(qtdGenes)] for y in range(qtdGenes)]
    
    # distancia entre as cidades
    for i in range(qtdGenes):
        for j in range(qtdGenes):
            d = math.sqrt(math.pow(cx[i] - cx[j], 2) + math.pow(cy[i] - cy[j], 2))
            dcidade[i][j] = round(d, 2)

    dist = [0 for x in range(qtdCromossomos)]

    # custo de cada cromossomo - a soma das distâncias para cada indivíduo
    for i in range(qtdCromossomos):
        for j in range(qtdGenes):
            # soma das distancias para cada cromossomo
            d = dist[i] + dcidade[tour[i][j]][tour[i][j+1]]
            dist[i] = round(d, 2)

    return dist

qtdCromossomos = 20
qtdGenes = 20

# Gera 20 cromossomos (caminhos) com 20 genes (cidades) cada um, com valores entre 0 e 19
# Matriz 20x20
for i in range(qtdGenes):
    cidades = [x for x in range(0, 20)]
    random.shuffle(cidades)
    cromossomos.append(cidades)

# Gera dois vetores de 20 posições cada com valores entre 0 e 1, que representarão os custos entre as cidades
# Matriz 1x20
cx = [round(random.random(), 2) for x in range(qtdGenes)]
cy = [round(random.random(), 2) for x in range(qtdGenes)]

dist = funcaoFitness(cromossomos, cx, cy)

# Ordena as listas de distancia e cromossomos com base nas distancias obtidas
dist, cromossomos = zip(*sorted(zip(dist, cromossomos)))

# Fatia a lista de cromossomos na metade, ficando apenas com os 10 melhores
cromossomosFatiados = cromossomos[0:10]

print(cromossomosFatiados)
print(len(cromossomosFatiados))