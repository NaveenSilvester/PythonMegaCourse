import FreeSimpleGUI as sg
import zipcreator as zc

label = sg.Text("Enter your name: ")
name_box = sg.InputText(tooltip="Etner your name", key ="NameBox")
add = sg.Button("Add", key="Add")
#add_button = sg.Button("Add")
selectFile = sg.Text("Selet File to Zip: ")
selectFile_box = sg.Input(tooltip="Enter the file location", key="FileLocationBox")
selectFile_button = sg.FilesBrowse("Browse File", key="FilesBrowseButton")

selectDestination = sg.Text("Select Destination Folder")
selectDestination_box = sg.Input(tooltip="Enter the file Destination", key="FileDestinationBox")
selectDestination_button = sg.FolderBrowse("Browse SelectDestination", key="FolderBrowse")

chooseButton = sg.Button("Compress", key="CompressButton")
outputLabel = sg.Text(key="output")

window = sg.Window('My Zipper App', layout=[[label, name_box, add],
                                            [selectFile, selectFile_box, selectFile_button], 
                                            [selectDestination, selectDestination_box, selectDestination_button], 
                                            [chooseButton, outputLabel]])


while True:
    (event, event_values) = window.read()

    print (event)
    print (event_values)

    match event:
        case "CompressButton":
            #print ("I am in")
            #print (f"Event Values are {event_values}, Len is {len(event_values)}")
            files = event_values["FilesBrowseButton"].split(";")
            folder = event_values["FolderBrowse"]
            #print (files)
            #print (folder)
            print (f"Type of Folder is : {type(folder)}")
            zc.make_archive(filepaths=files, dest_dir=folder)
            #zc.make_archive (filepaths=["todos.txt", "function.py"], dest_dir="dest" )
            window["output"].update("Compression Completed")

        case "Add":
            print (" am in ADD")
            #print (f"Event Values are {event_values}, Len is {len(event_values)}")
        case sg.WIN_CLOSED:
            break

window.close()

    