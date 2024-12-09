import FreeSimpleGUI
import FreeSimpleGUI as sg
import function
label = sg.Text("Type in a Todo")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add")

label2 =sg.Text("View Todos")
list_box = sg.Listbox(values=function.get_todos(), key="todos", enable_events= True, size=[45,10])
edit_button = sg.Button("Edit")
remove_button = sg.Button("Remove")

window = FreeSimpleGUI.Window('My Todo App', 
                              layout=[[label, input_box, add_button],
                                      [label2, list_box, edit_button, remove_button]
                                      ], 
                              font = ('Helvetica', 20))
#window.read()

while True:
    (event, event_values) = window.read()
    print (event)
    print ("Event Values : ",event_values)
    match event:
        case "Add":
            todos = function.get_todos()
            newtodo = event_values["todo"]
            newtodo = newtodo.strip("\n")
            #print ("LENGTH OF NEWTODO: ",len(newtodo))
            if (len(newtodo) > 1):
                newtodo = newtodo + "\n"
                todos.append(newtodo)
                function.write_todos(todos)
                window["todos"].update(values=todos)
        
        case "Edit":
            if len(event_values["todos"]) != 0:
                #print ("NUILLLLLLL")
                todo_to_edit = event_values["todos"][0]
                #print ("The Value selected for edit: ", todo_to_edit)
                new_todo = event_values["todo"]
                new_todo = new_todo.strip("\n")
                #print(f"Value of edited new todo is ", new_todo)
                if (len(new_todo) > 1):
                    todos = function.get_todos()
                    index = todos.index(todo_to_edit)
                    todos[index] = new_todo + "\n"
                    function.write_todos(todos)
                    window['todos'].update(values=todos)

        case "todos":
            window['todo'].update(value =event_values['todos'][0]) 

        case "Remove":
            if len(event_values["todos"]) != 0:
                removed_element = event_values["todos"][0]
                removed_element = removed_element.strip("\n")
                #print (f"Selected {removed_element} for removal")            
                removed_element_len = len(event_values["todos"])
                #print ("LEN is ", removed_element_len)
                if removed_element_len == 0:
                    print("NO Elements selected for removal")
                #print ("This is: ", values["todos"])
                if (removed_element_len)  >= 1:
                    
                    #print("The removed element is ", removed_element)
                    todos = function.get_todos()
                    index = todos.index(removed_element + "\n")
                    #print ("Index is : ", index)
                    todos.remove(todos[index])
                    #print ("New updated removed : ",todos)
                    function.write_todos(todos)
                    #print("New todo list is : ", function.get_todos())
                    todos = function.get_todos()
                    #print("This is teh Todo list for your referer: ", todos)
                    window['todos'].update(values=todos)

        case sg.WIN_CLOSED:
            break

window.close()
