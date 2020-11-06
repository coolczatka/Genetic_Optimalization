from Config import Config
from Config import ChromosomeConfig
import SelectionStrategy
from AckleyOptimalizer import AckleyOptimalizer

def main():
    chromosomeConfig = ChromosomeConfig()
    config = Config(1000, chromosomeConfig)
    ackleyOptimalization = AckleyOptimalizer(config)
    ackleyOptimalization.run()

if __name__ == '__main__':
    main()
