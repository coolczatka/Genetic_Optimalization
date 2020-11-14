from Config import Config, ChromosomeConfig, FunctionParameters
from math import pi
from XmlFile import XmlFileReader
import os

global config
global window

if(os.path.exists('config.xml')):
    reader = XmlFileReader('config.xml')
    config = reader.getConfig()
else:
    fc = FunctionParameters(20, 0.2, 2*pi)
    cc = ChromosomeConfig()
    config = Config(100, cc)
window = 1