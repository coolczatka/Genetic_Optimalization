from Config import Config
from Config import ChromosomeConfig
import SelectionStrategy
from AckleyOptimalizer import AckleyOptimalizer
from BinaryHelper import BinaryHelper
from Chromosome import Chromosome
from ClassicalGene import ClassicalGene
from Gui.Gui import Gui

#
def main():
    gui = Gui()
    gui.run()

if __name__ == '__main__':
    main()
