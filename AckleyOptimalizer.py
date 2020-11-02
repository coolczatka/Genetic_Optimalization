import math
import random
import numpy as np
from SelectionStrategy import SelectionStrategy
class AckleyOptimalizer():
    def __init__(self, config, a = 20, b = 0.2, c = 2*math.pi):
        self.config = config
        self.parameterA = a
        self.parameterB = b
        self.parameterC = c

        self.population = [[self.getRandomBinary(), self.getRandomBinary()] for i in range(self.config.populationSize)]

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
               - math.exp(sum(math.cos(self.parameterC*X))/len(X)) + self.parameterA + math.e

    def applicateSelection(self, X, Y):
        selectionStrategy = SelectionStrategy(X, Y)
        if(self.config.selection == 0):
            newX = selectionStrategy.best(self.config)

    def run(self):
        pass




