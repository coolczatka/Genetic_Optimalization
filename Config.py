from math import pi
class FunctionParameters:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class Config:
    #kind 0 - minimalization 1 - maximalization
    def __init__(self, generations, chromosomeConfig, kind=0, searchRange=(-30, 30), populationSize=500, selection=0, precision=6,
                  fp = FunctionParameters(20, 0.4, 2*pi), selectionParameter = 10, elitePercent=10):
        self.generations = generations
        self.kind = kind
        self.range = searchRange
        self.populationSize = populationSize
        self.chConfig = chromosomeConfig
        self.precision = precision
        #TODO config strategii czy zrobić nową klasę
        #0 - procent najlepszych 1 - turniejowa 2 - rankingowa 3 - kołem ruletki
        self.selection = selection
        self.selectionParameter = selectionParameter # procent najlepszych / ilosc osobnikow w turnieju
        self.elitePercent = elitePercent
        self.functionParameters = fp
        self.outputConfig = OutputConfig()

class ChromosomeConfig:
    """mk = rodzaj mutacji
    mp = prawdopodobienstwo mutacji
    ck = rodzaj krzyzowania
    cp = prawdopodobienstwo krzyzowania
    ip = prawdopodobieństwo inwersji"""
    def __init__(self, mk = 0, mp = 0.1, ck = 0, cp = .9, ip = .7):
        # 0 - brak
        # 1 - Brzegowa
        # 2 - Jednopunktowa
        # 3 - Dwupunktowa
        self.mk = mk
        self.mp = mp
        # 0 - brak
        # 1 - jednopunktowe settrings
        # 2 - dwupunktowe
        # 3 - jednorodna
        self.ck = ck
        self.cp = cp
        self.ip = ip

class OutputConfig:
    def __init__(self, exportToFile = True, savePlots = True):
        self.exportToFile = exportToFile
        self.savePlots = savePlots