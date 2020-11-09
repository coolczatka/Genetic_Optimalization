
class SelectionStrategy:

    def __init__(self):
        pass

    @staticmethod
    def best(population, percentOfBest):
        i = (len(population)*percentOfBest)/100
        print(i)
        specimens_to_cross = []
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
