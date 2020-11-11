import math
from random import randint


class SelectionStrategy:

    def __init__(self, config):
        self.config = config
        # pass

    def best(self, population):
        specimens_to_cross = []
        index = math.ceil((len(population) * self.config.winnersPercent) / 100)
        s = sorted(population, key=lambda specimen: specimen.value)

        for i in range(int(index)):
            specimens_to_cross.append(s[i])

        return specimens_to_cross

    def tournament(self, population):
        n = self.config.winnersPercent
        tournaments = self.divide_for_tournaments(n, population)
        winners = []
        for tournament in tournaments:
            winner = tournament[0]
            for contestant in tournament:
                if contestant.value < winner.value:
                    winner = contestant
            winners.append(winner)

        specimens_to_cross = winners

        return specimens_to_cross

    @staticmethod
    def divide_for_tournaments(n, population):
        k = math.ceil(len(population) / n)  # number of tournaments
        tournaments = []
        temp = population

        for j in range(n):
            t = []
            for i in range(int(k)):
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
