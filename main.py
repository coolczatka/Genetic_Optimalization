from Config import Config
from Config import ChromosomeConfig
import SelectionStrategy
from AckleyOptimalizer import AckleyOptimalizer
from BinaryHelper import BinaryHelper
from Chromosome import Chromosome
from ClassicalChromosome import ClassicalChromosome

def main():
    chromosomeConf = ChromosomeConfig(mk=1, ck=1)
    config = Config(1000, chromosomeConf)
    ao = AckleyOptimalizer(config)
    ao.run()
    # config = ChromosomeConfig(mp=1, cp=1, ip=1, mk=3, ck=3)
    # c1 = ClassicalChromosome((-10,10), 6)
    # c1.setConfig(config)
    # c2 = ClassicalChromosome((-10,10), 6)
    # c2.setConfig(config)
    #
    # c1.initializeBitString()
    # c2.initializeBitString()
    # print(c1)
    # c1 = c1.invert()
    # print(c1)

if __name__ == '__main__':
    main()
