from Config import Config, ChromosomeConfig, FunctionParameters
from math import pi

global config
global window

fc = FunctionParameters(20, 0.2, 2*pi)
cc = ChromosomeConfig()
config = Config(100, cc)

window = 1