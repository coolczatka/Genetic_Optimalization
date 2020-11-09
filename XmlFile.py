from datetime import datetime

class XmlFile:

    def __init__(self):
        folder = 'datasets/'
        extension = '.xml'

        now = datetime.now()
        name = folder + now.date().__str__() + f'_{now.hour}_{now.minute}_{now.second}'+extension
        self.file = open(name, 'a')
        self.generationCounter = 0

    def xmlStart(self, config, parameters):
        xmlText = '<?xml version="1.0" encoding="UTF-8"?>' + '<result>' + f'<startTime>{datetime.now()}</startTime>'

        configStr = '<config>'
        
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