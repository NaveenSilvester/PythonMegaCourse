import FreeSimpleGUI as sg
label = sg.Text("Type in a Todo")
input_box = sg.InputText(tooltip="Enter a todo")
add_button = sg.Button("Add")

selectFile = sg.Text("Selet File to Zip: ")
selectFile_box = sg.Input(tooltip="Enter the file location")
selectFile_button = sg.FileBrowse("Browse SelectFile")

selectDestination = sg.Text("Select Destination Folder")
selectDestination_box = sg.Input(tooltip="Enter the file Destination")
selectDestination_button = sg.FolderBrowse("Browse SelectDestination")

chooseButton = sg.Button("Compress")

window = sg.Window('My Zipper App', layout=[[label, input_box, add_button], 
                                            [selectFile, selectFile_box, selectFile_button], 
                                            [selectDestination, selectDestination_box, selectDestination_button], 
                                            [chooseButton]])
window.read()
window.close()


