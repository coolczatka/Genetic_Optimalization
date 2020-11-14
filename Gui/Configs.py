from Gui.AbstractSimpleGuiElement import AbstractSimpleGuiElement
import PySimpleGUI as sg
import math
import GC

class FunctionParametersInputs(AbstractSimpleGuiElement):
    @staticmethod
    def signalMapping():
        return {
            'CK': {'BRAK': 0, 'JEDNOPUNKTOWE': 1, 'DWUPUNKTOWE': 2, 'JEDNORODNE': 3},
            'MK': {'BRAK': 0, 'BRZEGOWA': 1, 'JEDNOPUNKTOWA': 2, 'DWUPUNKTOWA': 3},
            'KIND': {'MINIMALIZACJA': 0, 'MAKSYMALIZACJA': 1},
            'SELECTION': {'PROCENT NAJLEPSZYCH':0, 'TURNIEJOWA': 1, 'RANKINGOWA': 2, 'KOLEM RULETKI': 3}
        }
    @staticmethod
    def parameterName():
        return {
            'PROCENT NAJLEPSZYCH': 'Procent najlepszych',
            'TURNIEJOWA': 'Ilość uczestników turnieju',
            'RANKINGOWA': '',
            'KOLEM RULETKI': ''
        }
    def __init__(self):
        self.setSgClass(sgclass=None)
        definition = [
            [
                sg.Column([
                    [sg.Text('Parametry funkcji')],
                    [sg.Text('A'), sg.Input(key='_PARAMETER_A_', enable_events=True, default_text="20", size=(20,1))],
                    [sg.Text('B'), sg.Input(key='_PARAMETER_B_', enable_events=True, default_text="0.4", size=(20,1))],
                    [sg.Text('C'), sg.Input(key='_PARAMETER_C_', enable_events=True, default_text=str(2*math.pi), size=(20,1))],
                ]),
                sg.Column([
                    [sg.Text('Konfiguracja ogólna')],

                    [sg.Text('Ilość generacji'), sg.Input(key='_GENERATIONS_', enable_events=True, default_text="1000", size=(20,1))],
                    [sg.Text('Wielkość populacji'), sg.Input(key='_POPULATIONSIZE_', enable_events=True, default_text="500", size=(20,1))],
                    [sg.Text('Rodzaj'), sg.Combo(list(FunctionParametersInputs.signalMapping()['KIND'].keys()), default_value='MINIMALIZACJA', key='_KIND_', enable_events=True, size=(20,1))],
                    [sg.Text('Dokładność'), sg.Input(key='_PRECISION_', enable_events=True, default_text="6", size=(20,1))],
                    [sg.Text('Zakres'), sg.Input(key='_RANGE_', enable_events=True, default_text="-10,10", size=(20,1))],
                    [sg.Text('Selekcja'), sg.Combo(list(FunctionParametersInputs.signalMapping()['SELECTION'].keys()),default_value='PROCENT NAJLEPSZYCH', key='_SELECTION_', enable_events=True, size=(25, 1))],
                    [sg.Text('Procent elity'), sg.Input(key='_ELITE_PERCENT_', enable_events=True, default_text="10", size=(20,1))],

                    [sg.Text('Procent najlepszych', key='_SP_LABEL_'), sg.Input(key='_SELECTIONPARAMETER_', enable_events=True, default_text="10", size=(20,1))],
                ]),
                sg.Column([
                    [sg.Text('Konfiguracja chromosomów')],

                    [sg.Text('Rodzaj krzyżowania'),
                     sg.Combo(list(FunctionParametersInputs.signalMapping()['CK'].keys()), default_value='BRAK', key='_CK_',
                              enable_events=True, size=(20, 1))],
                    [sg.Text('Prawdopodobienstwo krzyżowania'),
                     sg.Input(key='_CP_', enable_events=True, default_text="0.9", size=(20, 1))],

                    [sg.Text('Rodzaj mutacji'),
                     sg.Combo(list(FunctionParametersInputs.signalMapping()['MK'].keys()), default_value='BRAK', key='_MK_',
                              enable_events=True, size=(20, 1))],
                    [sg.Text('Prawdopodobienstwo mutacji'),
                     sg.Input(key='_MP_', enable_events=True, default_text="0.9", size=(20, 1))],

                    [sg.Text('Prawdopodobienstwo inwersji'),
                     sg.Input(key='_IP_', enable_events=True, default_text="0.7", size=(20, 1))],
                ]),
            ],
        ]
        self.setDefinition(definition)
        self.instance = self.createElement()

    def getInstance(self):
        return self.instance

    def processSignals(self, args):
        event = args[0]
        values = args[1]

        if event == '_PARAMETER_A_' and values['_PARAMETER_A_'] and values['_PARAMETER_A_'][-1] not in ('0123456789.'):
            GC.window['_PARAMETER_A_'].update(values['_PARAMETER_A_'][:-1])
        elif event == '_PARAMETER_B_' and values['_PARAMETER_B_'] and values['_PARAMETER_B_'][-1] not in ('0123456789.'):
            GC.window['_PARAMETER_B_'].update(values['_PARAMETER_B_'][:-1])
        elif event == '_PARAMETER_C_' and values['_PARAMETER_C_'] and values['_PARAMETER_C_'][-1] not in ('0123456789.'):
            GC.window['_PARAMETER_C_'].update(values['_PARAMETER_C_'][:-1])
        elif event == '_SELECTION_':
            label = FunctionParametersInputs.parameterName()[values['_SELECTION_']]
            visible = True if len(label) > 0 else False
            GC.window['_SP_LABEL_'].update(label, visible=visible)
            #GC.window['_SELECTIONPARAMETER_'].update(visible=visible)

