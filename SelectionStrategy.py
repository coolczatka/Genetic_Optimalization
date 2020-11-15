import math
import random
import GC

class SelectionStrategy:

    def best(self, population):
        specimens_to_cross = self.getBest(population, GC.config.selectionParameter)

        return specimens_to_cross

    @staticmethod
    def getBest(population, percentOfChosen):
        best = []
        index = math.ceil((len(population) * percentOfChosen) / 100)
        s = sorted(population, key=lambda specimen: specimen.value)

        for i in range(int(index)):
            best.append(s[i])

        return best

    def tournament(self, population):
        n = int(GC.config.selectionParameter)
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
                x = random.randint(0, len(temp) - 1)
                t.append(temp[x])
                del temp[x]
            tournaments.append(t)
        return tournaments

    def rouletteWheel(self, population):  # trzeba znormalizowc
        reversed_population = [-1 * p.value for p in population]
        wheel = self.rouletteWheel_max(reversed_population)

        new_population = []
        while len(population) >= len(new_population):
            [temp] = random.choices(population, wheel)
            new_population.append(temp)
        return new_population

    @staticmethod
    def rouletteWheel_max(population):  # trzeba znormalizowc
        values = [p for p in population]
        if min(values) < 0:
            values = [v - min(values) + 1 for v in values]

        val_sum = sum(values)
        wheel = []
        for v in values:
            wheel.append(v / val_sum)
        return wheel

        #return matingSet, weights
