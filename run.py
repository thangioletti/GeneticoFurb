# Autores: Alex Seródio, Luma Kuhl, Matheus Losi e Tiago Henrique Angioletti

import random
import time
import genetico

start = time.time()

geracoes = 10000
taxaMutacao = 5
qtdCromossomos = 20
qtdGenes = 20

cromossomos = genetico.gerarPopulacao(qtdCromossomos, qtdGenes)
vx = genetico.gerarVetorDePosicoes(qtdGenes)
vy = genetico.gerarVetorDePosicoes(qtdGenes)

for ciclo in range(geracoes):

    dist = genetico.funcaoFitness(cromossomos, vx, vy)              # calcula a distância total de cada cromossomo
    dist, cromossomos = zip(*sorted(zip(dist, cromossomos)))        # ordena as listas de distancia e cromossomos com base nas distancias obtidas
    cromossomos = list(cromossomos[0:10])                           # fatia a lista de cromossomos na metade, mantendo apenas os 10 melhores (10 primeiros)

    roleta = genetico.construirRoleta(len(cromossomos))             # gera a roleta de possibilidades de cada cromossomo ser selecionado

    for i in range(taxaMutacao):
        pai1 = cromossomos[random.choice(roleta)].copy()            # seleciona um cromossomo aleatório com base a probabilidade da roleta para ser o pai1
        pai2 = cromossomos[random.choice(roleta)].copy()            # seleciona um cromossomo aleatório com base a probabilidade da roleta para ser o pai2
        
        filho1, filho2 = genetico.recombinacao(pai1, pai2)          # gera dois novos filhos com base na recombinação dos dois pais
        filho1, filho2 = genetico.mutacao(filho1, filho2)           # realiza uma mutação individual em cada um dos dois novos filhos

        cromossomos.append(filho1)                                  # insere o novo filho na lista de cromossomos
        cromossomos.append(filho2)                                  # insere o novo filho na lista de cromossomos

dist = genetico.funcaoFitness(cromossomos, vx, vy)                  # calcula os custos de cada cromossomo da geração final
dist, cromossomos = zip(*sorted(zip(dist, cromossomos)))            # ordena as listas de distancia e cromossomos com base nas distancias obtidas

melhorCusto = dist[0]                                               # recupera o melhor custo encontrado
melhorSolucao = cromossomos[0]                                      # recupera a melhor solução encontrada

tempoExecucao = round(time.time() - start, 2)

print("Tamanho da população: " + str(qtdCromossomos))
print("Taxa de Mutação: " + str(round(taxaMutacao/100, 2)))
print("Número de Cidades: " + str(qtdGenes))
print("Melhor Custo: " + str(melhorCusto))
print("Melhor Solução: " + str(melhorSolucao))
print("Tempo de execução do programa: " + str(tempoExecucao) + " segundos")