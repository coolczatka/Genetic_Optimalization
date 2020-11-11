from Gui.AbstractSimpleGuiElement import AbstractSimpleGuiElement
import PySimpleGUI as sg

class SimpleGuiMenuBar(AbstractSimpleGuiElement):

    def __init__(self, name = None):
        self.setName(name)
        self.setSgClass(sgclass=sg.Menu)
        definition = [['Plik', ['Open', 'Save', 'Exit',]],
                ['Informacje', 'Informacja'],]
        self.setDefinition(definition)
        self.instance = self.createElement()

    def processSignals(self, args):
        signal = args[0]
        values = args[1]
        if signal == 'Informacja':
            sg.popup('Projekt 1 Obliczenia Ewolucyjne 2020', title="Informacja")
        elif signal == 'Exit':
            args[0] = sg.WINDOW_CLOSED

    def getInstance(self):
        return self.instance

