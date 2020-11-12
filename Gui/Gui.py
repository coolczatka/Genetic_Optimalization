
import PySimpleGUI as sg
from Gui.Menubar import SimpleGuiMenuBar
from Gui.Configs import *
from Config import Config, ChromosomeConfig
from AckleyOptimizer import AckleyOptimizer
import GC
# Define the window's contents
class Gui:
    def __init__(self):
        menubar = SimpleGuiMenuBar()
        functionParameters = FunctionParametersInputs()

        self.components = [
            menubar,
        ]
        self.layout = [
            [menubar.getInstance()],
            [functionParameters.getInstance()],
            [sg.Button('START')]
        ]

        self.adaptLayout()

    def run(self):

        # Create the window
        #window = sg.Window('Window Title', layout, no_titlebar=True, location=(0, 0), size=(800, 600), keep_on_top=True)
        sg.theme('DarkAmber')
        window = sg.Window('Optymalizacja funkcji Ackleya', self.layout, size=(800, 600))

        # Display and interact with the Window using an Event Loop
        while True:
            event, values = window.read()
            args = [event, values]
            # See if user wants to quit or window was closed
            for i in self.components:
                i.processSignals(args)
            if args[0] == 'START':
                GC.config = self.makeConfig(args[1])
                aopt = AckleyOptimizer()
                aopt.run()
            if args[0] == sg.WINDOW_CLOSED:
                break
            # Output a message to the window
           # window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")

        # Finish up by removing from the screen
        window.close()

    def adaptLayout(self):
        for i in range(len(self.layout)):
            while(isinstance(self.layout[i][0], list)):
                listt = self.layout[i]
                self.layout.pop(i)
                index = i
                for ii in listt:
                    self.layout.insert(index, ii)
                    index+=1

    def makeConfig(self, values):
        chromosomeConfig = ChromosomeConfig(
            mk=FunctionParametersInputs.signalMapping()['MK'][values['_MK_']],
            mp=float(values['_MP_']),
            ck=FunctionParametersInputs.signalMapping()['CK'][values['_CK_']],
            cp=float(values['_CP_']),
            ip=float(values['_IP_'])
        )
        minRange, maxRange = values['_RANGE_'].split(',')
        config = Config(
            generations=int(values['_GENERATIONS_']),
            chromosomeConfig=chromosomeConfig,
            kind=FunctionParametersInputs.signalMapping()['KIND'][values['_KIND_']],
            searchRange=(float(minRange), float(maxRange)),
            populationSize=int(values['_POPULATIONSIZE_']),
            selection=FunctionParametersInputs.signalMapping()['SELECTION'][values['_SELECTION_']],
            precision=int(values['_PRECISION_']),
        )
        return config
