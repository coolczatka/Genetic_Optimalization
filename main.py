from Config import Config
import SelectionStrategy
from AckleyOptimalizer import AckleyOptimalizer

def main():
    config = Config(1000)
    ackleyOptimalization = AckleyOptimalizer(config)
    ackleyOptimalization.run()

if __name__ == '__main__':
    main()
