
import PySimpleGUI as sg

# Define the window's contents
layout = [[sg.Text("Proszę podać parametry? jakie? jeszcze nie wiem")],
          [sg.Input(key='-INPUT-')],
          #[sg.Text(size=(40, 1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
#window = sg.Window('Window Title', layout, no_titlebar=True, location=(0, 0), size=(800, 600), keep_on_top=True)
window = sg.Window('Optymalizacja funkcji Ackleya', layout, size=(800, 600))

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
   # window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()