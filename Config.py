

class Config:
    #kind 0 - minimalization 1 - maximalization
    def __init__(self, generations, chromosomeConfig, kind = 0, searchRange = (-30, 30), populationSize = 500, selection = 0):
        self.generations = generations
        self.kind = kind
        self.range = searchRange
        self.populationSize = populationSize
        self.selection = selection
        self.chConfig = chromosomeConfig


class ChromosomeConfig:
    #mk = rodzaj mutacji
    #mp = prawdopodobienstwo mutacji
    #ck = rodzaj krzyzowania
    #cp = prawdopodobienstwo krzyzowania
    def __init__(self, mk = 0, mp = 0.1, ck = 0, cp = .9):
        # 0 - brak
        # 1 - Brzegowa
        # 2 - Jednopunktowa settings {'mutation_points': [5]}
        # 3 - Dwupunktowa {'mutation_points': [1, 5]}
        self.mk = mk
        self.mp = mp
        # 0 - brak
        # 1 - jednopunktowe settrings {'crosspoints': [5]}
        # 2 - dwupunktowe settings {'crosspoints': [3, 5]}
        self.ck = ck
        self.cp = cp