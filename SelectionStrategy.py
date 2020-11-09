
class SelectionStrategy:

    def __init__(self, X, Y, elite = 0):
        self.X = X
        self.Y = Y
        self.elite = elite

    def best(self, percentOfBest):
        pass

    def tournament(self, amountOfTournaments):
        n = amountOfTournaments

        pass

    def ranking(self): # nie wiem jakie parametry
        pass

    def rouletteWheel(self): # trzeba znormalizowc
        pass
