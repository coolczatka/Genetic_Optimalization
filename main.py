from deap import creator
from deap import tools
from deap import base
import random
import math
import numpy as np
import matplotlib.pyplot as plt
from functions import SVCParameters, SVCParametersFitness, mutationSVC
from functions import DecisionTreeParameters, DecisionTreeParametersFitness, mutationDecisionTree
from functions import KNeighborsParameters, KNeighborsParametersFitness, mutationKNeighbors
from functions import MLPParameters, MLPParametersFitness, mutationMLP
from functions import NBParameters, NBParametersFitness, mutationNB

import pandas as pd
pd.set_option('display.max_columns', None)
#df=pd.read_csv("data.csv",sep=',')
df=pd.read_csv("glass.csv",sep=',')
print(df.columns)
#y=df['Status']
y=df['Type']
#df.drop('Status',axis=1,inplace=True)
df.drop('Type',axis=1,inplace=True)
#df.drop('ID',axis=1,inplace=True)
df.drop('Id',axis=1,inplace=True)
#df.drop('Recording',axis=1,inplace=True)
numberOfAtributtes= len(df.columns)

config = {
    'kind': 'Max',#NIE TESTOWAC Min, Max

    'selection': tools.selTournament,
    'selectionParameters': {
        'tournsize': 3
    },
    'mating': tools.cxTwoPoint,
    'matingParameters': {

    },
    'mutation': mutationNB,
    'mutationParameters': {
        #Gaussian
        # 'mu': 5,
        # 'sigma': 20,
        # 'indpb': 0.2
    },
    'sizePopulation': 50,
    'probabilityMutation': .2,
    'probabilityCrossover': .8,
    'numberIteration': 50,

    'range': (-10, 10)
}

def performFitness():
    if config['kind'] == 'Min':
        creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMin)
    else:
        creator.create("FitnessMax", base.Fitness, weights=(1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMax)
    toolbox = base.Toolbox()
    toolbox.register('individual', NBParameters, numberOfAtributtes, creator.Individual)
    toolbox.register('population', tools.initRepeat, list, toolbox.individual)
    toolbox.register('evaluate', NBParametersFitness,y,df,numberOfAtributtes)
    toolbox.register('select', config['selection'], **config['selectionParameters'])
    toolbox.register('mate', config['mating'], **config['matingParameters'])
    toolbox.register('mutate', config['mutation'], **config['mutationParameters'])

    pop = toolbox.population(n=config['sizePopulation'])
    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    result = {
        'mins': [],
        'maxs': [],
        'means': [],
        'stds': [],
        'bests': []
    }
    g = 0
    numberElitism = 1
    while g < config['numberIteration']:
        g = g + 1
        print("-- Generation %i --" % g)
        offspring = toolbox.select(pop, len(pop))
        offspring = list(map(toolbox.clone, offspring))
        listElitism = []
        for x in range(0, numberElitism):
            listElitism.append(tools.selBest(pop, 1)[0])
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < config['probabilityCrossover']:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values
        for mutant in offspring:
        # mutate an individual with probability MUTPB
            if random.random() < config['probabilityMutation']:
                toolbox.mutate(mutant)
                del mutant.fitness.values
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit
        print("  Evaluated %i individuals" % len(invalid_ind))
        pop[:] = offspring + listElitism
        fits = [ind.fitness.values[0] for ind in pop]
        length = len(pop)

        minValue = min(fits)
        maxValue = max(fits)
        mean = sum(fits) / length
        sum2 = sum(x * x for x in fits)
        std = abs(sum2 / length - mean ** 2) ** 0.5

        print("  Min %s" % min(fits))
        print("  Max %s" % max(fits))
        print("  Avg %s" % mean)
        print("  Std %s" % std)
        best_ind = tools.selBest(pop, 1)[0]
        print("Best individual is %s, %s" % (
        best_ind, best_ind.fitness.values[0]))

        result['mins'].append(minValue)
        result['maxs'].append(maxValue)
        result['means'].append(mean)
        result['stds'].append(std)
        result['bests'].append(best_ind.fitness.values[0])

    print("-- End of (successful) evolution --")
    return result

def drawPlots(data):
    plt.figure()
    plt.xlabel("Generation")
    plt.ylabel("Best")
    plt.plot(data['bests'])
    plt.show()

    plt.figure()
    plt.xlabel("Generation")
    plt.ylabel("Mean")
    plt.plot(data['means'])
    plt.show()

    plt.figure()
    plt.xlabel("Generation")
    plt.ylabel("Std")
    plt.plot(data['stds'])
    plt.show()
data = performFitness()
drawPlots(data)


