
import PySimpleGUI as sg
from Gui.Menubar import SimpleGuiMenuBar
from Gui.Configs import *
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
            [sg.Button('Ok'), sg.Button('Quit')]
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
            if args[0] == sg.WINDOW_CLOSED or event == 'Quit':
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