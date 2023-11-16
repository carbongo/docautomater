import PySimpleGUI as sg

# Define the layout of the GUI
layout = [
    [sg.Text('Select two files:')],
    [sg.Input(key='file1'), sg.FileBrowse(), sg.Input(key='file2'), sg.FileBrowse()],
    [sg.Button('Submit')]
]

# Create the window
window = sg.Window(title='File Selector', layout=layout, alpha_channel=1)

# Event loop
while True:
    event, values = window.read(close=True)
    if event == sg.WIN_CLOSED:
        break
    if event == 'Submit':
        file1 = values['file1']
        file2 = values['file2']
        # Generate some output based on the selected files
        output = f"You selected {file1} and {file2}"
        sg.popup(output)

# Close the window
window.close()
