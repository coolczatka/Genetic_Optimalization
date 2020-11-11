import math
from random import randint


class SelectionStrategy:

    def __init__(self):
        pass

    @staticmethod
    def best(population, percentOfBest):
        specimens_to_cross = []
        index = math.ceil((len(population) * percentOfBest) / 100)
        s = sorted(population, key=lambda specimen: specimen.fitness)

        for i in range(int(index)):
            specimens_to_cross.append(s[i])

        return specimens_to_cross

    @staticmethod
    def tournament(population, numberOfSpecimenInTournament):
        n = numberOfSpecimenInTournament
        k = math.ceil(len(population) / n)  # number of tournaments
        tournaments = []
        temp = population
        # podział na tournamenty
        for j in range(k):
            t = []
            for i in range(n):
                if len(temp) == 0:
                    break
                x = randint(0, len(temp) - 1)
                print(x)
                t.append(temp[x])
                del temp[x]
            tournaments.append(t)

        specimens_to_cross = []

        return specimens_to_cross

    def ranking(self):  # nie wiem jakie parametry
        pass

    def rouletteWheel(self):  # trzeba znormalizowc
        pass
