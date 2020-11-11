import math
from random import randint


class SelectionStrategy:

    def __init__(self, population):
        self.population = population
        # pass

    def best(self, percentOfBest):
        specimens_to_cross = []
        index = math.ceil((len(self.population) * percentOfBest) / 100)
        s = sorted(self.population, key=lambda specimen: specimen.value)

        for i in range(int(index)):
            specimens_to_cross.append(s[i])

        return specimens_to_cross

    def tournament(self, numberOfSpecimenInTournament):
        n = numberOfSpecimenInTournament
        tournaments = self.divide_for_tournaments(n)
        winners = []
        for tournament in tournaments:
            winner = tournament[0]
            for contestant in tournament:
                if contestant.value < winner.value:
                    winner = contestant
            winners.append(winner)

        specimens_to_cross = winners

        return specimens_to_cross

    def divide_for_tournaments(self, n):
        k = math.ceil(len(self.population) / n)  # number of tournaments
        tournaments = []
        temp = self.population

        for j in range(int(k)):
            t = []
            for i in range(n):
                if len(temp) == 0:
                    break
                x = randint(0, len(temp) - 1)
                t.append(temp[x])
                del temp[x]
            tournaments.append(t)
        return tournaments


    def ranking(self):  # nie wiem jakie parametry
        pass

    def rouletteWheel(self):  # trzeba znormalizowc
        pass
