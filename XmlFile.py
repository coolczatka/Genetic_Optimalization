from datetime import datetime
from xml.dom import minidom
from Config import Config, ChromosomeConfig

class XmlFileWriter:

    def __init__(self):
        folder = 'datasets/'
        extension = '.xml'

        now = datetime.now()
        name = folder + now.date().__str__() + f'_{now.hour}_{now.minute}_{now.second}'+extension
        self.file = open(name, 'a')
        self.generationCounter = 0

    def xmlStart(self, config, parameters):
        xmlText = '<?xml version="1.0" encoding="UTF-8"?>' + '<result>' + f'<startTime>{datetime.now()}</startTime>'

        #TODO Dodac wszystkie konfigi
        configStr = '<config>'
        configStr += f'<generationsCount>{config.generations}</generationsCount>'
        configStr += f'<kind>{config.kind}</kind>'
        configStr += f'<populationSize>{config.populationSize}</populationSize>'
        configStr += f'<selection>{config.selection}</selection>'
        configStr += f'<precision>{config.precision}</precision>'
        configStr += f"<functionParameters><a>{parameters['a']}</a><b>{parameters['b']}</b><c>{parameters['c']}</c></functionParameters>"
        configStr += f'<range><start>{config.range[0]}</start><end>{config.range[1]}</end></range>'
        configStr += f'<chromosomeConfig><ck>{config.chConfig.ck}</ck><cp>{config.chConfig.cp}</cp><mk>{config.chConfig.mk}</mk><mp>{config.chConfig.mp}</mp><ip>{config.chConfig.ip}</ip></chromosomeConfig>'
        configStr += '</config>'

        xmlText += configStr
        self.file.write(xmlText)

    def openGenerationsTag(self):
        self.file.write('<generations>')

    def addGeneration(self, generation):
        self.generationCounter += 1
        self.file.write(f'<generation number="{self.generationCounter}">')
        for individual in generation:
            individualXml = '<individual>'
            individualXml += f'<chromosome position="0">{individual[0].bitString}</chromosome>'
            individualXml += f'<chromosome position="1">{individual[1].bitString}</chromosome>'
            individualXml += '</individual>'
            self.file.write(individualXml)
        self.file.write('</generation>')

    def closeGenerationsTag(self):
        self.file.write('</generations>')

    def xmlEnd(self):
        xmlText = f'<endTime>{datetime.now()}</endTime>' + '</result>'
        self.file.write(xmlText)
        self.file.close()

class XmlFileReader:

    def __init__(self, name):
        self.directory = 'datasets/'
        self.xmlFile = minidom.parse(self.directory + name)
    #TODO Dodac wszystkie konfigi
    def getConfig(self):
        configxml = self.xmlFile.getElementsByTagName('config')[0]

        functionParametersXml = configxml.getElementsByTagName('functionParameters')[0]

        a = functionParametersXml.getElementsByTagName('a')[0].firstChild.nodeValue
        b = functionParametersXml.getElementsByTagName('b')[0].firstChild.nodeValue
        c = functionParametersXml.getElementsByTagName('c')[0].firstChild.nodeValue

        rangeXml = configxml.getElementsByTagName('range')[0]

        minRange = rangeXml.getElementsByTagName('start')[0].firstChild.nodeValue
        maxRange = rangeXml.getElementsByTagName('end')[0].firstChild.nodeValue

        generationsCount = configxml.getElementsByTagName('generationsCount')[0].firstChild.nodeValue
        kind = configxml.getElementsByTagName('kind')[0].firstChild.nodeValue
        populationSize = configxml.getElementsByTagName('populationSize')[0].firstChild.nodeValue
        selection = configxml.getElementsByTagName('selection')[0].firstChild.nodeValue
        precision = configxml.getElementsByTagName('precision')[0].firstChild.nodeValue

        chromosomeConfigXml = configxml.getElementsByTagName('chromosomeConfig')[0]

        ck = chromosomeConfigXml.getElementsByTagName('ck')[0].firstChild.nodeValue
        cp = chromosomeConfigXml.getElementsByTagName('cp')[0].firstChild.nodeValue
        mk = chromosomeConfigXml.getElementsByTagName('mk')[0].firstChild.nodeValue
        mp = chromosomeConfigXml.getElementsByTagName('mp')[0].firstChild.nodeValue
        ip = chromosomeConfigXml.getElementsByTagName('ip')[0].firstChild.nodeValue
        chromosomeConfig = ChromosomeConfig(mk, mp, ck, cp, ip)

        return Config(generationsCount, chromosomeConfig, kind, (minRange, maxRange), populationSize, selection,
                      precision)


