import math


class SelectionStrategy:

    def __init__(self):
        pass

    @staticmethod
    def best(population, percentOfBest):
        specimens_to_cross = []
        index = math.ceil((len(population)*percentOfBest)/100)
        s = sorted(population, key=lambda specimen: specimen.fitness)

        for i in range(int(index)):
            specimens_to_cross.append(s[i])

        return specimens_to_cross


    @staticmethod
    def tournament(amountOfTournaments):
        n = amountOfTournaments
        specimens_to_cross = []

        return specimens_to_cross

    def ranking(self): # nie wiem jakie parametry
        pass

    def rouletteWheel(self): # trzeba znormalizowc
        pass
