import numpy as np
import math

class Specimen:
    def __init__(self, genome, value, config):
        self.genome = genome
        self.value = value
        self.config = config

    def __str__(self):
        string = "Genome: "
        for x in self.genome:
            string = string + str(x) + " "

        string = string + " Value: " + str(self.value)
        return string

    def mating(self, partner):
        genome1 = []
        genome2 = []
        for i, j in zip(self.genome, partner.genome):
            #print(j)
            gene1, gene2 = i.cross(j)
            genome1.append(gene1)
            genome2.append(gene2)

        #print(genome1)
        #print(genome2[1])
        print(self.config.chConfig.ck)
        val1 = [gene.getValueFromBitString() for gene in genome1]
        val2 = [gene.getValueFromBitString() for gene in genome2]

        #print(val1)
        #print(val2)
        #print(genome2[1])

        newSpec1 = Specimen(genome1, self.ackley(val1), self.config)
        newSpec2 = Specimen(genome2, self.ackley(val2), self.config)
        return newSpec1, newSpec2

    def setGene(self, gene, pos):
        self.genome[pos] = gene

    def ackley(self, X):
        X = np.array(X)
        return -self.config.functionParameters.a * math.exp(-self.config.functionParameters.b * math.sqrt(sum(X**2)/len(X)))\
               -math.exp(sum([math.cos(self.config.functionParameters.c*x) for x in X])/len(X)) + self.config.functionParameters.a + math.e
