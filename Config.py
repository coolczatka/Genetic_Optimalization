

class Config:
    #kind 0 - minimalization 1 - maximalization
    def __init__(self, generations, chromosomeConfig, kind=0, searchRange=(-30, 30), populationSize=500, selection=0, precision=6,
                  winnersPercent=10, elitePercent=10):
        self.generations = generations
        self.kind = kind
        self.range = searchRange
        self.populationSize = populationSize
        self.chConfig = chromosomeConfig
        self.precision = precision
        #TODO config strategii czy zrobić nową klasę
        self.selection = selection
        self.winnersPercent = winnersPercent
        self.elitePercent = elitePercent


class ChromosomeConfig:
    """mk = rodzaj mutacji
    mp = prawdopodobienstwo mutacji
    ck = rodzaj krzyzowania
    cp = prawdopodobienstwo krzyzowania
    ip = prawdopodobieństwo inwersji"""
    def __init__(self, mk = 0, mp = 0.1, ck = 0, cp = .9, ip = .7):
        # 0 - brak
        # 1 - Brzegowa
        # 2 - Jednopunktowa settings {'mutation_points': [5]}
        # 3 - Dwupunktowa {'mutation_points': [1, 5]}
        self.mk = mk
        self.mp = mp
        # 0 - brak
        # 1 - jednopunktowe settrings {'crosspoints': [5]}
        # 2 - dwupunktowe settings {'crosspoints': [3, 5]}
        # 3 - jednorodna
        self.ck = ck
        self.cp = cp
        self.ip = ip


        #self.validateSettings()

    def validateSettings(self):
        if(self.mk == 2):
            if(len(self.settings['mutation_points']) != 1):
                raise ValueError('Błędna długość mutation_points dla mutacji jednopunktowej')
        if (self.mk == 3):
            if (len(self.settings['mutation_points']) != 2):
                raise ValueError('Błędna długość mutation_points dla mutacji dwupunktowej')

        if (self.ck == 1):
            if (len(self.settings['crosspoints']) != 1):
                raise ValueError('Błędna długość crosspoints dla krzyzowania jednopunktowego')
        if (self.mk == 2):
            if (len(self.settings['crosspoints']) != 2):
                raise ValueError('Błędna długość crosspoints dla krzyzowania dwupunktowego')