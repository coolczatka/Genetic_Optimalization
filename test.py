from AckleyOptimizer import AckleyOptimizer
from Config import ChromosomeConfig, Config
from SelectionStrategy import SelectionStrategy

chromosomeConf = ChromosomeConfig(mk=1, ck=1)
config = Config(1000, chromosomeConf, populationSize=421)
#print(421*10/100)

ao = AckleyOptimizer(config)

for s in ao.population:
    print(str(s))
print("""aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa""")


newpop = ao.lifecycle()
for s in newpop:
    print(str(s))
ao.population = newpop

