import FreeSimpleGUI as sg
label_feet = sg.Text("Enter feet")
inputFt = sg.InputText(tooltip="Enter Feet value")
label_inches = sg.Text("Enter Inches")
inputIn = sg.InputText(tooltip="Enter Inches")
close_button = sg.Button("Convert")
window = sg.Window("Converter", layout=[[label_feet, inputFt],[label_inches, inputIn],[close_button]])
window.read()
window.close()