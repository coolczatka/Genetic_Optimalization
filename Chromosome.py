from random import randint, random
from BinaryHelper import BinaryHelper

class Chromosome():

    #ChromosomeConfig
    def setConfig(self, config):
        self.config = config

    def __init__(self, length = 0):
        self.x = randint(-1*2**(length), 2**length-1)
        self.y = randint(-1*2**(length), 2**length-1)
        self.binaryX = BinaryHelper.binary(self.x)
        self.binaryY = BinaryHelper.binary(self.y)
        self.chromosomeString = self.binaryX + self.binaryY

    def splitChromosomeStringToBinaries(self):
        self.binaryX = self.chromosomeString[:32]
        self.binaryY = self.chromosomeString[32:]

    @staticmethod
    def createFromChromosomeString(string, config):
        newChromosome = Chromosome()
        newChromosome.setConfig(config)
        newChromosome.chromosomeString = string
        newChromosome.splitChromosomeStringToBinaries()
        newChromosome.x = BinaryHelper.floatVal(newChromosome.binaryX)
        newChromosome.y = BinaryHelper.floatVal(newChromosome.binaryY)
        return newChromosome

    def cross(self, chromB):
        if self.config.ck == 1:
            pass
        elif self.config.ck == 2:
            pass

    def mutate(self):
        #Brzegowa
        newChromosomeString = self.chromosomeString
        if self.config.mk == 1:
            rand = random()
            if rand <= self.config.mp:
                newChromosomeString[-1] = BinaryHelper.flipByte(newChromosomeString[-1])
        #jednopunktowa
        elif self.config.mk == 2:
            if(random() <= self.config.mp):
                position = randint(0, len(self.chromosomeString)-1)
                newChromosomeString[position] = BinaryHelper.flipByte(newChromosomeString[position])
        #dwupunktowa
        elif self.config.mk == 3:
            if(random() <= self.config.mp):
                position1 = randint(0, len(newChromosomeString) - 1)
                position2 = randint(0, len(newChromosomeString) - 1)
                while position1 == position2:
                    position2 = randint(0, len(newChromosomeString) - 1)
                newChromosomeString[position1] = BinaryHelper.flipByte(newChromosomeString[position1])
                newChromosomeString[position2] = BinaryHelper.flipByte(newChromosomeString[position2])
        newChromosome = Chromosome.createFromChromosomeString(newChromosomeString, self.config)
        return newChromosome



