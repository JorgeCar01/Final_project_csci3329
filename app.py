import PySimpleGUI as sg
from filesorterFun import file_moving

sg.theme('Dark Blue 3')  # please make your windows colorful


layout1 = [
            [sg.Text('Please enter the Folder to be sorted and it destination')],
            [sg.Text('Folder to be sorted', size=(15, 1)), sg.InputText('', key='-INITIAL-'), sg.FolderBrowse()],
            [sg.Text('Destination Folder', size=(15, 1)), sg.InputText('', key='-LOCATION-'), sg.FolderBrowse()],
            [],
            [sg.Text('Would you like a prefix to attach to the sorted folders name? (Leave empty if do not wish to enter a prefix)')],
            [sg.InputText('', key='-INPUTTEXT-')],
            [sg.Submit(), sg.Exit()]
            ]




window = sg.Window('Simple data entry window', layout1)
event, values = window.read()
if values["-INPUTTEXT-"] == "":
    x = file_moving(values["-INITIAL-"], values["-INITIAL-"], values["-LOCATION-"])
else:
    x = file_moving(values["-INITIAL-"], values["-INPUTTEXT-"], values["-LOCATION-"])
    
if event == 'Submit':
    x.initialize_file_sorting()


window.close()