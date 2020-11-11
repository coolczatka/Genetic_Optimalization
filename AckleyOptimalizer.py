import math
import random
import numpy as np
from SelectionStrategy import SelectionStrategy
from ClassicalGene import ClassicalGene
from Specimen import Specimen
from XmlFile import XmlFile

class AckleyOptimalizer():
    def __init__(self, config, a=20, b=0.2, c=2*math.pi):
        self.config = config
        self.parameterA = a
        self.parameterB = b
        self.parameterC = c

        self.population = []
        for i in range(self.config.populationSize):
            x = ClassicalGene(self.config.range, self.config.precision)
            x.initializeBitString()
            y = ClassicalGene(self.config.range, self.config.precision)
            y.initializeBitString()

            genome = [x, y]
            gen_values = [x.getValueFromBitString(), y.getValueFromBitString()]
            s = Specimen(genome, self.ackley(gen_values))
            self.population.append(s)

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
        return -self.parameterA * math.exp(-self.parameterB * math.sqrt(sum(X**2)/len(X)))\
               -math.exp(sum([math.cos(self.parameterC*x) for x in X])/len(X)) + self.parameterA + math.e

    def applySelection(self, X, Y):
        selection_strategy = SelectionStrategy(self.config)
        if self.config.selection == 0:
            newX = selection_strategy.best(self.population)

    def run(self):
        xmlFile = XmlFile()
        parameters = {'a': self.parameterA, 'b': self.parameterB, 'c': self.parameterC}
        xmlFile.xmlStart(self.config, parameters)
        xmlFile.openGenerationsTag()
        xmlFile.addGeneration([(i.genome[0], i.genome[1]) for i in self.population])
        xmlFile.closeGenerationsTag()
        xmlFile.xmlEnd()




