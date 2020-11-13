import PySimpleGUI as sg

class AbstractSimpleGuiElement:

    def setSgClass(self, sgclass):
        self.sgClass = sgclass

    def setDefinition(self, definition):
        self.definition = definition

    def createElement(self):
        if(self.sgClass != None):
            return self.sgClass(self.definition)
        else:
            return self.definition

    def processSignals(self, args):
        raise NotImplementedError('NI')
