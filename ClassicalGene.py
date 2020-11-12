import math
from random import randint, random
from AbstractChromosome import AbstractChromosome
from BinaryHelper import BinaryHelper
import GC

class ClassicalGene(AbstractChromosome):
    def __init__(self, range, precision):
        #a,b - przedział
        self.b = range[1]
        self.a = range[0]
        self.precision = precision
        self.bitlength = math.ceil(math.log2((self.b-self.a)*(10**precision)))
        self.bitString = ''

    def initializeBitString(self):
        bitString = ''
        for i in range(int(self.bitlength)):
            bitString = bitString + str(randint(0, 1))
        self.bitString = bitString
        return bitString

    def getValueFromBitString(self):
        print(self.bitString)
        return self.a + int(self.bitString, 2) * (self.b - self.a) / ((2**self.bitlength) - 1)

    def cross(self, chromB):
        if(random() < GC.config.chConfig.cp):
            a = self.crossW(chromB)
            b = chromB.crossW(self)
            return a, b
        return self, chromB

    def crossW(self, chromB):
        newChromosomeString = ''
        noCrossover = False
        # 1 - jednopunktowe settrings {'crosspoints': [5]}
        # 2 - dwupunktowe settings {'crosspoints': [3, 5]}
        # 3 - jednorodna
        if GC.config.chConfig.ck == 1:
            point = randint(1, len(self.bitString) - 1)
            newChromosomeString = self.bitString[:point] + chromB.bitString[point:]
        elif GC.config.chConfig.ck == 2:
            point1 = randint(1, len(self.bitString) - 1)
            point2 = randint(1, len(self.bitString) - 1)
            while point2 == point1:
                point2 = randint(1, len(self.bitString) - 1)
            if(point2 < point1):
                temp = point2
                point2 = point1
                point1 = temp
            newChromosomeString = self.bitString[:point1]
            newChromosomeString = newChromosomeString + chromB.bitString[point1:point2]
            newChromosomeString = newChromosomeString + self.bitString[point2:]
        elif GC.config.chConfig.ck == 3:
            for i in range(len(self.bitString)):
                if(i % 2 == 0):
                    newChromosomeString = newChromosomeString + self.bitString[i]
                else:
                    newChromosomeString = newChromosomeString + chromB.bitString[i]
        else:
            return self
        newChromosome = ClassicalGene.createFromChromosomeString(newChromosomeString, (self.a, self.b),
                                                             self.precision)
        return newChromosome

    def mutate(self):
        # Brzegowa
        newChromosomeString = self.bitString
        if GC.config.chConfig.mk == 1:
            rand = random()
            if rand <= GC.config.chConfig.mp:
                length = len(newChromosomeString)
                newChromosomeString = newChromosomeString[:length-1] + BinaryHelper.flipByte(newChromosomeString[-1])
        # jednopunktowa
        elif GC.config.chConfig.mk == 2:
            if (random() <= GC.config.chConfig.mp):
                position = randint(0, len(newChromosomeString) - 1)
                newChromosomeString = newChromosomeString[:position] + BinaryHelper.flipByte(newChromosomeString[position]) + newChromosomeString[position+1:]
        # dwupunktowa
        elif GC.config.chConfig.mk == 3:
            if (random() <= GC.config.chConfig.mp):
                position1 = randint(0, len(newChromosomeString) - 1)
                position2 = randint(0, len(newChromosomeString) - 1)
                while position1 == position2:
                    position2 = randint(0, len(newChromosomeString) - 1)
                if(position1 > position2):
                    temp = position1
                    position1 = position2
                    position2 = temp
                newChromosomeString2 = newChromosomeString[:position1] + BinaryHelper.flipByte(newChromosomeString[position1])
                newChromosomeString2 += newChromosomeString[position1+1:position2] + BinaryHelper.flipByte(newChromosomeString[position2])
                newChromosomeString2 += newChromosomeString[position2+1:]
                newChromosomeString = newChromosomeString2
        else:
            return self
        newChromosome = ClassicalGene.createFromChromosomeString(newChromosomeString, (self.a, self.b), self.precision, GC.config.chConfig)
        return newChromosome

    @staticmethod
    def createFromChromosomeString(string, range, precision, chromosomeConfig):
        cc = ClassicalGene(range, precision, chromosomeConfig)
        cc.bitString = string
        return cc

    def invert(self):
        newChromosomeString = self.bitString
        if(random() <= GC.config.chConfig.ip):
            position1 = randint(0, len(newChromosomeString) - 1)
            position2 = randint(0, len(newChromosomeString) - 1)
            while position1 == position2:
                position2 = randint(0, len(newChromosomeString) - 1)
            if (position1 > position2):
                temp = position1
                position1 = position2
                position2 = temp
            newChromosomeString2 = newChromosomeString[:position1]
            newChromosomeString2 += newChromosomeString[position2:position1:-1]
            newChromosomeString2 += newChromosomeString[position2:]
            newChromosomeString = newChromosomeString2
        newChromosome = ClassicalGene.createFromChromosomeString(newChromosomeString, (self.a, self.b),
                                                                 self.precision, GC.config.chConfig)
        return newChromosome

    def __str__(self):
        return self.bitString



