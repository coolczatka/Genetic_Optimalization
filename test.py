from AckleyOptimalizer import AckleyOptimalizer
from Config import ChromosomeConfig, Config
from SelectionStrategy import SelectionStrategy

chromosomeConf = ChromosomeConfig(mk=1, ck=1)
config = Config(1000, chromosomeConf, populationSize=421)
#print(421*10/100)
ao = AckleyOptimalizer(config)
selection = SelectionStrategy(ao.population)

tc = selection.best(config.winnersPercent)
tour = selection.tournament(config.winnersPercent)

for s in tour:
    print(str(s))
