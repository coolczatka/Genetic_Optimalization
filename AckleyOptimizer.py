import math
import random
import numpy as np
from SelectionStrategy import SelectionStrategy
from ClassicalGene import ClassicalGene
from Specimen import Specimen
from XmlFile import XmlFileWriter


class AckleyOptimizer:

    def __init__(self, config):
        self.config = config

        self.population = []
        for i in range(self.config.populationSize):
            x = ClassicalGene(self.config.range, self.config.precision, self.config.chConfig)
            x.initializeBitString()
            y = ClassicalGene(self.config.range, self.config.precision, self.config.chConfig)
            y.initializeBitString()

            genome = [x, y]
            gen_values = [x.getValueFromBitString(), y.getValueFromBitString()]
            s = Specimen(genome, self.ackley(gen_values), self.config)
            self.population.append(s)

    def setPopulation(self, population):
        self.population = population

    def getRandomBinary(self):
        return bin((1 << self.bitlength) - 1 & random.randint(self.config.range[0], self.config.range[1]))

    @property
    def bitlength(self):
        i = 1
        while(2**i < max(abs(self.config.range[0]), abs(self.config.range[1]))):
            i = i + 1
        return i

    def ackley(self, X):
        X = np.array(X)
        return -self.config.functionParameters.a * math.exp(-self.config.functionParameters.b * math.sqrt(sum(X**2)/len(X)))\
               -math.exp(sum([math.cos(self.config.functionParameters.c*x) for x in X])/len(X)) + self.config.functionParameters.a + math.e

    def getBestOfGeneration(self):
        s = sorted(self.population, key=lambda specimen: specimen.value)
        best = s[0]
        return best

    def applySelection(self):
        selection_strategy = SelectionStrategy(self.config)
        if self.config.selection == 0:
            matingSet = selection_strategy.best(self.population)
            weights = [1 for m in matingSet]
        elif self.config.selection == 1:
            matingSet = selection_strategy.tournament(self.population)
            weights = [1 for m in matingSet]
        elif self.config.selection == 2:
            pass
        elif self.config.selection == 3:
            pass
        return matingSet, weights

    def lifecycle(self):
        newPopulation = []
        n = len(self.population)
        eliteLen = 0
        if self.config.elitePercent > 0:
            elite = SelectionStrategy.getBest(self.population, self.config.elitePercent)
            eliteLen = len(elite)
            newPopulation = newPopulation + elite
        selected, weights = self.applySelection()
        temp = selected
        while len(newPopulation) < n:
            #print("\n selected: ", selected, weights, "\n eliteLen: ", eliteLen, "\n sellen: ", len(selected), "\nweights len", len(weights) )
            parent1 = random.choices(temp, weights)
            parent2 = random.choices(temp, weights)
            #print(parent2[0])
            child1, child2 = parent1[0].mating(parent2[0])
            newPopulation.append(child1)
            if len(newPopulation) == n:
                break
            else:
                newPopulation.append(child2)
        #print(" ", eliteLen, " ", n )
        for i in range(eliteLen, n):
            for j in range(len(newPopulation[i].genome)):
                x = newPopulation[i].genome[j]
                x = x.mutate()
                x = x.invert()
                newPopulation[i].genome[j] = x

        return newPopulation

    def runGenerations(self):
        best = []
        for i in range(self.config.generations):
            newpop = self.lifecycle()
            self.population = newpop
            bestSpecimen = self.getBestOfGeneration()
            best.append(bestSpecimen)
        return best

    def run(self):
        xmlFile = XmlFileWriter()
        xmlFile.xmlStart(self.config)
        xmlFile.openGenerationsTag()
        xmlFile.addGeneration([(i.genome[0], i.genome[1]) for i in self.population])
        xmlFile.closeGenerationsTag()
        xmlFile.xmlEnd()





