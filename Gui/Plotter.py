import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import PySimpleGUI as sg
import matplotlib

from Gui.AbstractSimpleGuiElement import AbstractSimpleGuiElement


class Plotter(AbstractSimpleGuiElement):
    def processSignals(self, args):
        pass

    def __init__(self):
        matplotlib.use('TkAgg')
        self.setSgClass(sgclass=None)
        definition = [sg.Column(
            layout=[
                [sg.Canvas(key='fig_cv',
                           # it's important that you set this size
                           size=(400 * 2, 400)
                          )]
                ],
                background_color='#DAE0E6',
                pad=(0, 0)
                )]
        self.setDefinition(definition)
        self.instance = self.createElement()

    def getInstance(self):
        return self.instance

# t = np.arange(0, 3, .01)
# fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

    @staticmethod
    def best_by_generations_plot(x, y):
        plt.figure(1)
        fig = plt.gcf()
        DPI = fig.get_dpi()
        #fig.set_size_inches(404 * 2 / float(DPI), 404 / float(DPI))
        #x = np.linspace(0, 2 * np.pi)
        #y = np.sin(x)
        plt.plot(x, y)  # y best values, x - number of generation
        plt.title("Best of generation by generations")
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.grid()
        
        return fig

    @staticmethod
    def mean_plot(x, y):
        plt.figure(1)
        fig = plt.gcf()
        DPI = fig.get_dpi()
        # fig.set_size_inches(404 * 2 / float(DPI), 404 / float(DPI))
        # x = np.linspace(0, 2 * np.pi)
        # y = np.sin(x)
        plt.plot(x, y)  # y best values, x - number of generation
        plt.title("Mean of population")
        plt.xlabel('Mean')
        plt.ylabel('Generation')
        plt.grid()

        return fig

    @staticmethod
    def std_plot(x, y):
        plt.figure(1)
        fig = plt.gcf()
        DPI = fig.get_dpi()
        # fig.set_size_inches(404 * 2 / float(DPI), 404 / float(DPI))
        # x = np.linspace(0, 2 * np.pi)
        # y = np.sin(x)
        plt.plot(x, y)  # y best values, x - number of generation
        plt.title("Std of population")
        plt.xlabel('Std')
        plt.ylabel('Generation')
        plt.grid()

        return fig

    @staticmethod
    def draw_figure(canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg

    @staticmethod
    def draw_figure_(canvas, fig):
        if canvas.children:
            for child in canvas.winfo_children():
                child.destroy()
        figure_canvas_agg = FigureCanvasTkAgg(fig, master=canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='right', fill='both', expand=1)
