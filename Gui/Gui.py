
import PySimpleGUI as sg
from Gui.Menubar import SimpleGuiMenuBar
from Gui.Configs import *
from Config import Config, ChromosomeConfig
from AckleyOptimizer import AckleyOptimizer
# Define the window's contents
from Gui.Plotter import Plotter
import GC
from datetime import datetime
from time import time
class Gui:

    def __init__(self):
        menubar = SimpleGuiMenuBar()
        self.bestPlotter = Plotter('best')
        self.meanPlotter = Plotter('mean')
        self.stdPlotter = Plotter('std')

        functionParameters = FunctionParametersInputs()

        self.components = [
            menubar,
            functionParameters

        ]
        self.layout = [
            [menubar.getInstance()],
            [functionParameters.getInstance()],
            [sg.Button('START'), sg.Text('Czas wykonania: ', size=(20,1), font="Helvetica 10", key='_TIME_LABEL_')],
            [self.bestPlotter.getInstance()]
        ]

        self.adaptLayout()

    def run(self):

        # Create the window
        #window = sg.Window('Window Title', layout, no_titlebar=True, location=(0, 0), size=(800, 600), keep_on_top=True)
        sg.theme('DarkAmber')
        GC.window = sg.Window('Optymalizacja funkcji Ackleya', self.layout, size=(800, 600))

        # Display and interact with the Window using an Event Loop
        while True:
            event, values = GC.window.read()
            args = [event, values]
            # See if user wants to quit or window was closed
            for i in self.components:
                i.processSignals(args)
            if args[0] == 'START':
                GC.config = self.makeConfig(args[1])
                aopt = AckleyOptimizer()
                startTime = time()
                best, means, stds = aopt.run()
                endTime = time()
                duration = endTime-startTime
                print(duration)
                label = 'Czas wykonania: ' + str(round(endTime-startTime, 2)) + 's'
                print(label)
                GC.window['_TIME_LABEL_'].update(label)
                best_values = [b.value for b in best]

                folder = 'datasets/'
                extension = '.png'

                now = datetime.now()
                prefix = folder + now.date().__str__() + f'_{now.hour}_{now.minute}_{now.second}'

                x = range(GC.config.generations)
                bestFigure = self.bestPlotter.best_by_generations_plot(x, best_values)
                meanFigure = self.meanPlotter.mean_plot(x, means)
                stdFigure = self.stdPlotter.std_plot(x, stds)

                if(GC.config.outputConfig.savePlots):
                    bestFigure.savefig(prefix+'_best'+extension)
                    meanFigure.savefig(prefix+'_mean'+extension)
                    stdFigure.savefig(prefix+'_std'+extension)

                self.bestPlotter.draw_figure_(GC.window['best'].TKCanvas, bestFigure)
            if args[0] == sg.WINDOW_CLOSED:
                break
            # Output a message to the window
           # window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")

        # Finish up by removing from the screen
        GC.window.close()

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
        oc = GC.config.outputConfig
        minRange, maxRange = values['_RANGE_'].split(',')
        config = Config(
            generations=int(values['_GENERATIONS_']),
            chromosomeConfig=chromosomeConfig,
            kind=FunctionParametersInputs.signalMapping()['KIND'][values['_KIND_']],
            searchRange=(float(minRange), float(maxRange)),
            populationSize=int(values['_POPULATIONSIZE_']),
            selection=FunctionParametersInputs.signalMapping()['SELECTION'][values['_SELECTION_']],
            precision=int(values['_PRECISION_']),
            selectionParameter=float(values['_SELECTIONPARAMETER_']),
            elitePercent=float(values['_ELITE_PERCENT_']),
        )
        config.outputConfig = oc
        return config
