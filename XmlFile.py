from datetime import datetime
from xml.dom import minidom
from Config import Config, ChromosomeConfig, FunctionParameters, OutputConfig
import GC
class XmlFileWriter:

    def __init__(self, name=''):
        if(name == ''):
            folder = 'datasets/'
            extension = '.xml'

            now = datetime.now()
            name = folder + now.date().__str__() + f'_{now.hour}_{now.minute}_{now.second}'+extension
        self.file = open(name, 'w')
        self.generationCounter = 0

    def configXml(self, config):
        configStr = '<config>'
        configStr += f'<generationsCount>{config.generations}</generationsCount>'
        configStr += f'<kind>{config.kind}</kind>'
        configStr += f'<populationSize>{config.populationSize}</populationSize>'
        configStr += f'<selection>{config.selection}</selection>'
        configStr += f'<precision>{config.precision}</precision>'
        configStr += f"<functionParameters><a>{config.functionParameters.a}</a><b>{config.functionParameters.b}</b><c>{config.functionParameters.c}</c></functionParameters>"
        configStr += f'<range><start>{config.range[0]}</start><end>{config.range[1]}</end></range>'
        configStr += f'<chromosomeConfig><ck>{config.chConfig.ck}</ck><cp>{config.chConfig.cp}</cp><mk>{config.chConfig.mk}</mk><mp>{config.chConfig.mp}</mp><ip>{config.chConfig.ip}</ip></chromosomeConfig>'

        configStr += f'<selectionParameter>{config.selectionParameter}</selectionParameter>'
        configStr += f'<elitePercent>{config.elitePercent}</elitePercent>'

        configStr += f'<outputConfig><exportToFile>{int(config.outputConfig.exportToFile)}</exportToFile><savePlots>{int(config.outputConfig.savePlots)}</savePlots><newPlotForEachStart>{int(config.outputConfig.newPlotForEachStart)}</newPlotForEachStart></outputConfig>'

        configStr += '</config>'
        return configStr

    def xmlStart(self):
        xmlText = '<?xml version="1.0" encoding="UTF-8"?>' + '<result>' + f'<startTime>{datetime.now()}</startTime>'
        self.file.write(xmlText)

    def addConfig(self, config):
        configStr = self.configXml(config)
        self.file.write(configStr)

    def openGenerationsTag(self):
        self.file.write('<generations>')

    def addGeneration(self, population):
        self.generationCounter += 1
        self.file.write(f'<generation number="{self.generationCounter}">')
        for specimen in population:
            sign = 1 if GC.config.kind == 0 else -1
            individualXml = '<specimen>'
            individualXml += f'<value>{sign*specimen.value}</value>'
            for i, gene in enumerate(specimen.genome):
                individualXml += f'<gene position="{i}"><bitvalue>{gene.bitString}</bitvalue><value>{gene.getValueFromBitString()}</value></gene>'
            individualXml += '</specimen>'
            self.file.write(individualXml)
        self.file.write('</generation>')

    def closeGenerationsTag(self):
        self.file.write('</generations>')

    def xmlEnd(self):
        xmlText = f'<endTime>{datetime.now()}</endTime>' + '</result>'
        self.file.write(xmlText)
        self.file.close()

    def fileWriteAndClose(self, string):
        self.file.write(string)
        self.file.close()

class XmlFileReader:

    def __init__(self, name):
        self.xmlFile = minidom.parse(name)

    def getConfig(self):
        configxml = self.xmlFile.getElementsByTagName('config')[0]

        functionParametersXml = configxml.getElementsByTagName('functionParameters')[0]

        a = functionParametersXml.getElementsByTagName('a')[0].firstChild.nodeValue
        b = functionParametersXml.getElementsByTagName('b')[0].firstChild.nodeValue
        c = functionParametersXml.getElementsByTagName('c')[0].firstChild.nodeValue
        fp = FunctionParameters(a, b, c)

        rangeXml = configxml.getElementsByTagName('range')[0]

        minRange = rangeXml.getElementsByTagName('start')[0].firstChild.nodeValue
        maxRange = rangeXml.getElementsByTagName('end')[0].firstChild.nodeValue

        generationsCount = configxml.getElementsByTagName('generationsCount')[0].firstChild.nodeValue
        kind = configxml.getElementsByTagName('kind')[0].firstChild.nodeValue
        populationSize = configxml.getElementsByTagName('populationSize')[0].firstChild.nodeValue
        selection = configxml.getElementsByTagName('selection')[0].firstChild.nodeValue
        precision = configxml.getElementsByTagName('precision')[0].firstChild.nodeValue
        selectionParameter = configxml.getElementsByTagName('selectionParameter')[0].firstChild.nodeValue
        elitePercent = configxml.getElementsByTagName('elitePercent')[0].firstChild.nodeValue

        chromosomeConfigXml = configxml.getElementsByTagName('chromosomeConfig')[0]

        ck = chromosomeConfigXml.getElementsByTagName('ck')[0].firstChild.nodeValue
        cp = chromosomeConfigXml.getElementsByTagName('cp')[0].firstChild.nodeValue
        mk = chromosomeConfigXml.getElementsByTagName('mk')[0].firstChild.nodeValue
        mp = chromosomeConfigXml.getElementsByTagName('mp')[0].firstChild.nodeValue
        ip = chromosomeConfigXml.getElementsByTagName('ip')[0].firstChild.nodeValue
        chromosomeConfig = ChromosomeConfig(int(mk), mp, int(ck), cp, ip)

        outputConfigXml = configxml.getElementsByTagName('outputConfig')[0]
        exportToFile = outputConfigXml.getElementsByTagName('exportToFile')[0].firstChild.nodeValue
        savePlots = outputConfigXml.getElementsByTagName('savePlots')[0].firstChild.nodeValue
        newPlotForEachStart = outputConfigXml.getElementsByTagName('newPlotForEachStart')[0].firstChild.nodeValue

        oc = OutputConfig(exportToFile, savePlots, newPlotForEachStart)

        config = Config(
            generations=generationsCount,
            chromosomeConfig=chromosomeConfig,
            kind=int(kind),
            searchRange=(minRange, maxRange),
            populationSize=populationSize,
            selection=int(selection),
            precision=precision,
            fp=fp,
            selectionParameter=selectionParameter,
            elitePercent=elitePercent
        )
        config.outputConfig = oc
        # print(config.kind)
        return config

def exportConfig(config):
    file = XmlFileWriter('config.xml')
    xmlStr = '<?xml version="1.0" encoding="UTF-8"?>'
    xmlStr += file.configXml(config)
    file.fileWriteAndClose(xmlStr)

