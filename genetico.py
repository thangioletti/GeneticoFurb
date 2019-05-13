# Autores: Alex Seródio, Luma Kuhl, Matheus Losi e Tiago Henrique Angioletti

import random
import math

# Gera 20 cromossomos (populacao) com 20 genes (cidades) cada um, com valores entre 0 e 19
# Retorna matriz de 20x20
def gerarPopulacao(qtdCromossomos, qtdGenes):
    cromossomos = []
    for i in range(qtdCromossomos):
        cidades = [x for x in range(1, qtdGenes)]
        random.shuffle(cidades)
        cromossomos.append(cidades)
    return cromossomos

# Gera dois vetores de 20 posições cada com valores entre 0 e 1, que representarão os custos entre as cidades
# Retorna vetor de 20 posições
def gerarVetorDePosicoes(qtdGenes):
    return [round(random.random(), 2) for x in range(qtdGenes)]

# Inverte o gene selecionado (corte) entre os dois cromossomos
def trocarGenes(cromossomo1, cromossomo2, posGene):
    temp = cromossomo1[posGene]
    cromossomo1[posGene] = cromossomo2[posGene]
    cromossomo2[posGene] = temp

# Com base no cromossomo informado, localiza a posição de um gene duplicado, caso houver
# Retorna a posição do gene duplicaod se houver um ou -1 caso contrário
def localizarGeneDuplicado(cromossomo, corte):
    qtdGenes = len(cromossomo)
    for i in range(qtdGenes): 
        k = i + 1
        for j in range(k, qtdGenes): 
            if cromossomo[i] == cromossomo[j]: 
                if(i != corte):
                    return i
    return -1

# Calcula o custo de cada cromossomo utilizando os vetores vx e vy como base no calculo da distância total de cada cromossomo (custo)
# Retorna uma lista contendo o custo de cada cromossomo
def funcaoFitness(populacao, vx, vy):
    qtdCromossomos = len(populacao)
    qtdGenes = len(populacao[0])
    
    tour = [x + [x[0]] for x in populacao]                              # gera matriz 20x21 da populacao com última coluna sendo cópia da primeira

    dcidade = [[0 for x in range(qtdGenes)] for y in range(qtdGenes)]   # inicializa matriz de 20x20 com valor 0 em todas as posições
    dist = [0 for x in range(qtdCromossomos)]                           # inicializa lista com valor 0 em todas as posições
    
    # calculo da distância entre as cidades
    for i in range(qtdGenes):
        for j in range(qtdGenes):
            d = math.sqrt(math.pow(vx[i] - vx[j], 2) + math.pow(vy[i] - vy[j], 2))
            dcidade[i][j] = round(d, 2)

    # calculo do custo de cada cromossomo (soma das distâncias para cada indivíduo)
    for j in range(qtdCromossomos):
        for k in range(qtdGenes):
            d = dist[j] + dcidade[tour[j][k]-1][tour[j][k+1]-1]
            dist[j] = round(d, 2)

    return dist

# Constrói a roleta contendo 10 repetições do melhor cromossomo e decrementando em um o número de repetições 
# para cada cromossomo seguinte, para que os melhores cromossomos tenham uma chance maior de serem selecionados.
# Retorna uma lista com as probabilidades de cada cromossomo ser selecionado
def construirRoleta(qtdCromossomos):
    roleta = []
    count = qtdCromossomos-1
    for i in range(qtdCromossomos):
        for x in (range(i+1)):
            roleta.append(count)
        count-=1
    return roleta

# Faz a combinação dos dois cromossomos
def recombinacao(cromossomo1, cromossomo2):
    qtdGenes = len(cromossomo1)
    corte = random.randrange(0, qtdGenes-1)
    trocarGenes(cromossomo1, cromossomo2, corte)

    while corte != -1:
        trocarGenes(cromossomo1, cromossomo2, corte)
        corte = localizarGeneDuplicado(cromossomo1, corte)

    return cromossomo1, cromossomo2

# Realiza uma mutação nos dois cromossomos separadamente, selecionando dois genes específicos de cada cromossomo e os invertendo
# Retorna os dois cromossomos com a mutação
def mutacao(cromossomo1, cromossomo2):
    qtdGenes = len(cromossomo1)

    random1 = random.randrange(0, qtdGenes-1)
    random2 = random.randrange(0, qtdGenes-1)
    temp = cromossomo1[random1]
    cromossomo1[random1] = cromossomo1[random2]
    cromossomo1[random2] = temp

    random1 = random.randrange(0, qtdGenes-1)
    random2 = random.randrange(0, qtdGenes-1)
    temp = cromossomo2[random1]
    cromossomo2[random1] = cromossomo2[random2]
    cromossomo2[random2] = temp

    return cromossomo1, cromossomo2