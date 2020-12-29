from deap import creator
from deap import tools
from deap import base
import random
import math
import numpy as np
import matplotlib.pyplot as plt

config = {
    'a': 20,
    'b': 0.2,
    'c': 2*math.pi,
    'kind': 'Min',#NIE TESTOWAC Min, Max

    'selection': tools.selTournament, #TESTOWAC selTournament, selRandom, selBest, selWorst, selRoulette
    'selectionParameters': {
        'tournsize': 3
    },
    'mating': tools.cxTwoPoint, #TESTOWAC cxTwoPoint, cxOnePoint, cxUniform
    'matingParameters': {

    },
    'mutation': tools.mutGaussian, #TESTOWAC mutGaussian, mutShuffleIndexes, mutFlipBit
    'mutationParameters': {
        #Gaussian
        'mu': 5,
        'sigma': 20,
        'indpb': 0.2
    },
    'sizePopulation': 100,
    'probabilityMutation': .2,
    'probabilityCrossover': .8,
    'numberIteration': 100,

    'range': (-10, 10)
}


def individual(icls):
    genome = list()
    genome.append(random.uniform(config['range'][0],config['range'][1]))
    genome.append(random.uniform(config['range'][0],config['range'][1]))
    return icls(genome)

def fitnessFunction(individual):
    X = np.array(individual)
    return tuple([-config['a'] * math.exp(-config['b'] * math.sqrt(sum(X**2)/len(X)))\
           -math.exp(sum([math.cos(config['c']*x) for x in X])/len(X)) + config['a'] + math.e])

def performFitness():
    if config['kind'] == 'Min':
        creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMin)
    else:
        creator.create("FitnessMax", base.Fitness, weights=(1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMax)
    toolbox = base.Toolbox()
    toolbox.register('individual', individual, creator.Individual)
    toolbox.register('population', tools.initRepeat, list, toolbox.individual)
    toolbox.register('evaluate', fitnessFunction)
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
    plt.ylabel("Best")
    plt.plot(data['stds'])
    plt.show()
data = performFitness()
drawPlots(data)


