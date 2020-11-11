

class AbstractSimpleGuiElement:

    def setSgClass(self, sgclass):
        self.sgClass = sgclass

    def setName(self, name):
        self.name = name

    def setDefinition(self, definition):
        self.definition = definition

    def createElement(self):
        if(self.name != None):
            return self.sgClass(self.definition, key=self.name)
        else:
            return self.sgClass(self.definition)
    def processSignals(self, args):
        raise NotImplementedError('NI')