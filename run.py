import random
import math

qtdCromossomos = 20
qtdGenes = 20
cromossomos = []

def troca(pai1, pai2, corte):
    j = pai1[corte]
    pai1[corte] = pai2[corte]
    pai2[corte] = j

def find_duplicate(x, corte):
    _size = len(x) 
    repeated = [] 
    for i in range(_size): 
        k = i + 1
        for j in range(k, _size): 
            if x[i] == x[j] and x[i] not in repeated: 
                if(i != corte):
                    return i
    return -1

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

for ciclo in range(2):
    dist = funcaoFitness(cromossomos, cx, cy)

    # Ordena as listas de distancia e cromossomos com base nas distancias obtidas
    dist, cromossomos = zip(*sorted(zip(dist, cromossomos)))

    # Fatia a lista de cromossomos na metade, ficando apenas com os 10 melhores
    cromossomosFatiados = list(cromossomos[0:10])

    # Roleta
    roleta = []
    count = 9
    for i in range(10):
        for x in (range(i+1)):
            roleta.append(count)
        count=count-1

    # Sorteia os pais para gerar filhos
    for i in range(5):
        pai1 = cromossomosFatiados[random.choice(roleta)]
        pai2 = cromossomosFatiados[random.choice(roleta)]
        corte = random.randrange(0,19)
        troca(pai1, pai2, corte)

        while find_duplicate(pai1, corte) != -1:
            corte = find_duplicate(pai1, corte)
            troca(pai1, pai2, corte)

        # mutação
        random1 = random.randrange(0, 19)
        random2 = random.randrange(0, 19)
        
        j = pai1[random1]
        pai1[random1] = pai1[random2]
        pai1[random2] = j

        j = pai2[random1]
        pai2[random1] = pai2[random2]
        pai2[random2] = j

        cromossomosFatiados.append(pai1)
        cromossomosFatiados.append(pai2)

    cromossomos = cromossomosFatiados
    print('repete')
    # saída final eh o custo do melhor (primeiro depois de 10.000) e o próprio cromossomo

dist = funcaoFitness(cromossomos, cx, cy)

# Ordena as listas de distancia e cromossomos com base nas distancias obtidas
dist, cromossomos = zip(*sorted(zip(dist, cromossomos)))
print(cromossomos[0])
print(dist[0])

