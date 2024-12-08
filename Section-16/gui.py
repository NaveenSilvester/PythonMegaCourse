import FreeSimpleGUI
import FreeSimpleGUI as sg
label = sg.Text("Type in a Todo")
input_box = sg.InputText(tooltip="Enter a todo")
add_button = sg.Button("Add")

window = FreeSimpleGUI.Window('My Todo App', layout=[[label, input_box, add_button]])
window.read()
window.close()