

class Config:
    #kind 0 - minimalization 1 - maximalization
    def __init__(self, generations, kind = 0, searchRange = (-30, 30), populationSize = 500, selection = 0):
        self.generations = generations
        self.kind = kind
        self.range = searchRange
        self.populationSize = populationSize
        self.selection = selection