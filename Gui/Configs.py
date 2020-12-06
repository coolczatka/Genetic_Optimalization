from Gui.AbstractSimpleGuiElement import AbstractSimpleGuiElement
import PySimpleGUI as sg
import GC

class FunctionParametersInputs(AbstractSimpleGuiElement):
    @staticmethod
    def signalMapping():
        return {
            'CK': {'BRAK': 0, 'ARYTMETYCZNE': 1, 'HEURYSTYCZNE': 2},
            'MK': {'BRAK': 0, 'RÓWNOMIERNA': 1},
            'KIND': {'MINIMALIZACJA': 0, 'MAKSYMALIZACJA': 1},
            'SELECTION': {'PROCENT NAJLEPSZYCH':0, 'TURNIEJOWA': 1, 'KOLEM RULETKI': 3},
            'PLOT_TYPE': {'NAJLEPSZY Z POPULACJI W GENERACJI':0, 'SREDNIA Z POPULACJI W GENERACJI':1, 'ODCHYLENIE STANDARDOWE W GENERACJI':2}
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
        CK_map = {v: k for k, v in FunctionParametersInputs.signalMapping()['CK'].items()}
        MK_map = {v: k for k, v in FunctionParametersInputs.signalMapping()['MK'].items()}
        KIND_map = {v: k for k, v in FunctionParametersInputs.signalMapping()['KIND'].items()}
        SELECTION_map = {v: k for k, v in FunctionParametersInputs.signalMapping()['SELECTION'].items()}
        self.setSgClass(sgclass=None)
        definition = [
            [
                sg.Column([
                    [sg.Text('Parametry funkcji')],
                    [sg.Text('A'), sg.Input(key='_PARAMETER_A_', enable_events=True, default_text=str(GC.config.functionParameters.a), size=(20,1))],
                    [sg.Text('B'), sg.Input(key='_PARAMETER_B_', enable_events=True, default_text=str(GC.config.functionParameters.b), size=(20,1))],
                    [sg.Text('C'), sg.Input(key='_PARAMETER_C_', enable_events=True, default_text=str(GC.config.functionParameters.c), size=(20,1))],
                ]),
                sg.Column([
                    [sg.Text('Konfiguracja ogólna')],

                    [sg.Text('Ilość generacji'), sg.Input(key='_GENERATIONS_', enable_events=True, default_text=str(GC.config.generations), size=(20,1))],
                    [sg.Text('Wielkość populacji'), sg.Input(key='_POPULATIONSIZE_', enable_events=True, default_text=str(GC.config.populationSize), size=(20,1))],
                    [sg.Text('Rodzaj'), sg.Combo(list(FunctionParametersInputs.signalMapping()['KIND'].keys()), default_value=KIND_map[GC.config.kind], key='_KIND_', enable_events=True, size=(20,1))],
                    [sg.Text('Dokładność'), sg.Input(key='_PRECISION_', enable_events=True, default_text=str(GC.config.precision), size=(20,1))],
                    [sg.Text('Zakres'), sg.Input(key='_RANGE_', enable_events=True, default_text=str(str(GC.config.range[0])+','+str(GC.config.range[1])), size=(20,1))],
                    [sg.Text('Selekcja'), sg.Combo(list(FunctionParametersInputs.signalMapping()['SELECTION'].keys()),default_value=SELECTION_map[GC.config.selection], key='_SELECTION_', enable_events=True, size=(25, 1))],
                    [sg.Text('Procent elity'), sg.Input(key='_ELITE_PERCENT_', enable_events=True, default_text=str(GC.config.elitePercent), size=(20,1))],

                    [sg.Text('Procent najlepszych', key='_SP_LABEL_'), sg.Input(key='_SELECTIONPARAMETER_', enable_events=True, default_text=str(GC.config.selectionParameter), size=(20,1))],
                ]),
                sg.Column([
                    [sg.Text('Konfiguracja chromosomów')],

                    [sg.Text('Rodzaj krzyżowania'),
                     sg.Combo(list(FunctionParametersInputs.signalMapping()['CK'].keys()), default_value=CK_map[GC.config.chConfig.ck], key='_CK_',
                              enable_events=True, size=(20, 1))],
                    [sg.Text('Prawdopodobienstwo krzyżowania'),
                     sg.Input(key='_CP_', enable_events=True, default_text=str(GC.config.chConfig.cp), size=(20, 1))],

                    [sg.Text('Rodzaj mutacji'),
                     sg.Combo(list(FunctionParametersInputs.signalMapping()['MK'].keys()), default_value=MK_map[GC.config.chConfig.mk], key='_MK_',
                              enable_events=True, size=(20, 1))],
                    [sg.Text('Prawdopodobienstwo mutacji'),
                     sg.Input(key='_MP_', enable_events=True, default_text=str(GC.config.chConfig.mp), size=(20, 1))],
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
        #pilnowanie typow
        if event == '_PARAMETER_A_' and values['_PARAMETER_A_'] and values['_PARAMETER_A_'][-1] not in ('0123456789.'):
            GC.window['_PARAMETER_A_'].update(values['_PARAMETER_A_'][:-1])
        elif event == '_PARAMETER_B_' and values['_PARAMETER_B_'] and values['_PARAMETER_B_'][-1] not in ('0123456789.'):
            GC.window['_PARAMETER_B_'].update(values['_PARAMETER_B_'][:-1])
        elif event == '_PARAMETER_C_' and values['_PARAMETER_C_'] and values['_PARAMETER_C_'][-1] not in ('0123456789.'):
            GC.window['_PARAMETER_C_'].update(values['_PARAMETER_C_'][:-1])
        elif event == '_GENERATIONS_' and values['_GENERATIONS_'] and values['_GENERATIONS_'][-1] not in ('0123456789'):
            GC.window['_GENERATIONS_'].update(values['_GENERATIONS_'][:-1])
        elif event == '_POPULATIONSIZE_' and values['_POPULATIONSIZE_'] and values['_POPULATIONSIZE_'][-1] not in ('0123456789'):
            GC.window['_POPULATIONSIZE_'].update(values['_POPULATIONSIZE_'][:-1])
        elif event == '_PRECISION_' and values['_PRECISION_'] and values['_PRECISION_'][-1] not in ('0123456789'):
            GC.window['_PRECISION_'].update(values['_PRECISION_'][:-1])
        elif event == '_RANGE_' and values['_RANGE_'] and values['_RANGE_'][-1] not in ('0123456789.,'):
            GC.window['_RANGE_'].update(values['_RANGE_'][:-1])
        elif event == '_ELITE_PERCENT_' and values['_ELITE_PERCENT_'] and values['_ELITE_PERCENT_'][-1] not in ('0123456789.'):
            GC.window['_ELITE_PERCENT_'].update(values['_ELITE_PERCENT_'][:-1])
        elif event == '_SELECTIONPARAMETER_' and values['_SELECTIONPARAMETER_'] and values['_SELECTIONPARAMETER_'][-1] not in ('0123456789.'):
            GC.window['_SELECTIONPARAMETER_'].update(values['_SELECTIONPARAMETER_'][:-1])
        elif event == '_CP_' and values['_CP_'] and values['_CP_'][-1] not in ('0123456789.'):
            GC.window['_CP_'].update(values['_CP_'][:-1])
        elif event == '_MP_' and values['_MP_'] and values['_MP_'][-1] not in ('0123456789.'):
            GC.window['_MP_'].update(values['_MP_'][:-1])
        elif event == '_IP_' and values['_IP_'] and values['_IP_'][-1] not in ('0123456789.'):
            GC.window['_IP_'].update(values['_IP_'][:-1])

        #reszta
        elif event == '_SELECTION_':
            label = FunctionParametersInputs.parameterName()[values['_SELECTION_']]
            visible = True if len(label) > 0 else False
            GC.window['_SP_LABEL_'].update(label)#, visible=visible)
            #GC.window['_SELECTIONPARAMETER_'].update(visible=visible)

