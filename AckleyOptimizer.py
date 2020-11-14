import math
import random
import numpy as np
from SelectionStrategy import SelectionStrategy
from ClassicalGene import ClassicalGene
from Specimen import Specimen
from XmlFile import XmlFileWriter
import GC

class AckleyOptimizer:

    def __init__(self):

        self.population = []
        for i in range(GC.config.populationSize):
            x = ClassicalGene(GC.config.range, GC.config.precision)
            x.initializeBitString()
            y = ClassicalGene(GC.config.range, GC.config.precision)
            y.initializeBitString()

            genome = [x, y]
            gen_values = [x.getValueFromBitString(), y.getValueFromBitString()]
            s = Specimen(genome, self.ackley(gen_values))
            self.population.append(s)

    def setPopulation(self, population):
        self.population = population

    def ackley(self, X):
        X = np.array(X)
        return -GC.config.functionParameters.a * math.exp(-GC.config.functionParameters.b * math.sqrt(sum(X**2)/len(X)))\
               -math.exp(sum([math.cos(GC.config.functionParameters.c*x) for x in X])/len(X)) + GC.config.functionParameters.a + math.e

    def getBestOfGeneration(self):
        s = sorted(self.population, key=lambda specimen: specimen.value)
        best = s[0]
        return best

    def getMeanOfGeneration(self):
        specimenValues = [sp.value for sp in self.population]
        return np.mean(specimenValues)

    def getStdOfGeneration(self):
        specimenValues = [sp.value for sp in self.population]
        return np.std(specimenValues)

    def applySelection(self):
        selection_strategy = SelectionStrategy()
        if GC.config.selection == 0:
            matingSet = selection_strategy.best(self.population)
            weights = [1 for m in matingSet]
        elif GC.config.selection == 1:
            matingSet = selection_strategy.tournament(self.population)
            weights = [1 for m in matingSet]
        elif GC.config.selection == 2:
            pass
        elif GC.config.selection == 3:
            pass
        return matingSet, weights

    def lifecycle(self):
        newPopulation = []
        n = len(self.population)
        eliteLen = 0
        if GC.config.elitePercent > 0:
            elite = SelectionStrategy.getBest(self.population, GC.config.elitePercent)
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
        means = []
        stds = []
        for i in range(GC.config.generations):
            newpop = self.lifecycle()
            self.population = newpop
            bestSpecimen = self.getBestOfGeneration()
            mean = self.getMeanOfGeneration()
            std = self.getStdOfGeneration()
            best.append(bestSpecimen)
            means.append(mean)
            stds.append(std)
        return best, means, stds

    def run(self):
        best = []
        if(GC.config.outputConfig.exportToFile):
            best = []
            means = []
            stds = []

            xmlFile = XmlFileWriter()
            xmlFile.xmlStart(GC.config)
            xmlFile.openGenerationsTag()
            for i in range(GC.config.generations):
                newpop = self.lifecycle()
                self.population = newpop
                xmlFile.addGeneration(self.population)
                bestSpecimen = self.getBestOfGeneration()
                mean = self.getMeanOfGeneration()
                std = self.getStdOfGeneration()
                best.append(bestSpecimen)
                means.append(mean)
                stds.append(std)
            xmlFile.closeGenerationsTag()
            xmlFile.xmlEnd()
            return best, means, stds
        else:
            return self.runGenerations()





