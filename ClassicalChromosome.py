import math
from random import randint, random
from AbstractChromosome import AbstractChromosome
from BinaryHelper import BinaryHelper


class ClassicalChromosome(AbstractChromosome):
    def __init__(self, range, precission):
        self.b = range[1]
        self.a = range[0]
        self.precission = precission
        self.bitlength = math.ceil(math.log2((self.b-self.a)*(10**precission)))
        self.bitString = ''

    def initializeBitString(self):
        bitString = ''
        for i in range(self.bitlength):
            bitString = bitString + str(randint(0, 1))
        self.bitString = bitString
        return bitString

    def getValueFromBitString(self):
        return self.a + int(self.bitString, 2) * (self.b - self.a) / ((2**self.bitlength) - 1)

    def cross(self, chromB):
        a = self.crossW(chromB)
        b = chromB.crossW(self)
        return a, b

    def crossW(self, chromB):
        newChromosomeString = ''
        # 1 - jednopunktowe settrings {'crosspoints': [5]}
        # 2 - dwupunktowe settings {'crosspoints': [3, 5]}
        # 3 - jednorodna
        if self.config.ck == 1:
            if(random() <= self.config.cp):
                point = randint(1, len(self.bitString) - 1)
                newChromosomeString = self.bitString[:point] + chromB.bitString[point:]
        elif self.config.ck == 2:
            if(random() <= self.config.cp):
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
        elif self.config.ck == 3:
            if random() <= self.config.cp:
                for i in range(len(self.bitString)):
                    if(i % 2 == 0):
                        newChromosomeString = newChromosomeString + self.bitString[i]
                    else:
                        newChromosomeString = newChromosomeString + chromB.bitString[i]
        else:
            return self
        newChromosome = ClassicalChromosome.createFromChromosomeString(newChromosomeString, (self.a, self.b),
                                                                       self.precission)
        return newChromosome


    def mutate(self):
        # Brzegowa
        newChromosomeString = self.bitString
        if self.config.mk == 1:
            rand = random()
            if rand <= self.config.mp:
                length = len(newChromosomeString)
                newChromosomeString = newChromosomeString[:length-1] + BinaryHelper.flipByte(newChromosomeString[-1])
        # jednopunktowa
        elif self.config.mk == 2:
            if (random() <= self.config.mp):
                position = randint(0, len(newChromosomeString) - 1)
                newChromosomeString = newChromosomeString[:position] + BinaryHelper.flipByte(newChromosomeString[position]) + newChromosomeString[position+1:]
        # dwupunktowa
        elif self.config.mk == 3:
            if (random() <= self.config.mp):
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
        newChromosome = ClassicalChromosome.createFromChromosomeString(newChromosomeString, (self.a, self.b), self.precission)
        return newChromosome

    @staticmethod
    def createFromChromosomeString(string, range, precission):
        cc = ClassicalChromosome(range, precission)
        cc.bitString = string
        return cc

    def invert(self):
        newChromosomeString = self.bitString
        if(random() <= self.config.ip):
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
        newChromosome = ClassicalChromosome.createFromChromosomeString(newChromosomeString, (self.a, self.b),
                                                                       self.precission)
        return newChromosome
    def __str__(self):
        return self.bitString



