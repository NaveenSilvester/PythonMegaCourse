import FreeSimpleGUI as sg
 
label = sg.Text("What are dolphins?")
option1 = sg.Radio("Amphibians", group_id="question1")
option2 = sg.Radio("Fish", group_id="question1")
option3 = sg.Radio("Mammals", group_id="question1")
option4 = sg.Radio("Birds", group_id="question1")

 
label2 = sg.Text("What are dolphins?")
option2_1 = sg.Radio("Amphibians", group_id="question2")
option2_2 = sg.Radio("Fish", group_id="question2")
option2_3 = sg.Radio("Mammals", group_id="question2")
option2_4 = sg.Radio("Birds", group_id="question2")



window = sg.Window("Quiz",
                   layout=[[label],
                           [option1, option2,option3, option4],
                           [label2], [option2_1], [option2_2], [option2_3], [option2_4],                        
                           ])
 
window.read()
window.close()