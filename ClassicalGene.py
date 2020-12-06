import math
from random import randint, random
from AbstractChromosome import AbstractChromosome
from BinaryHelper import BinaryHelper
import GC
import copy

class ClassicalGene(AbstractChromosome):
    def __init__(self, range, precision):
        #a,b - przedział
        self.b = range[1]
        self.a = range[0]
        self.precision = precision
        self.value = randint(self.a, self.b)

    def initializeBitString(self):
        self.value = random()*(self.b-self.a)+self.a
        return self.value

    def getValueFromBitString(self):
        #print(self.bitString)
        return self.value

    def cross(self, chromB):
        if(random() < GC.config.chConfig.cp):
            a = self.crossW(chromB)
            b = chromB.crossW(self)
            return a, b
        return self, chromB

    def crossW(self, chromB):
        k = random()
        newGene = copy.deepcopy(self)
        if GC.config.chConfig.mk == 1:
            newGene.value = k * self.value + (1 - k) * chromB.value
        elif GC.config.chConfig.mk == 2:
            x1, x2 = sorted([self.value, chromB.value])
            newGene.value = k * (x2 - x1) + x1
        return newGene

    def mutate(self):
        # Brzegowa
        newGene = copy.deepcopy(self)
        if GC.config.chConfig.mk == 1:
            rand = random()
            if rand <= GC.config.chConfig.mp:
                newGene.value = random()*(self.b-self.a)+self.a
        return newGene

    def __str__(self):
            return self.value



