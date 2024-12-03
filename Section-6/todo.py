
while True:
    user_action = input("Type add, show, edit, complete or exit : ")
    user_action = user_action.strip()
    options = ["add", "show", "edit", "complete", "exit", "quit", "Quit", "Exit"]

    if user_action in options:
        match user_action:
            case 'add':
                file = open ('todos.txt','r')
                todos = file.readlines()
                file.close()

                todo = input("Enter a todo: \n") + "\n"
                todos.append(todo)
                file = open ("todos.txt", 'w')
                file.writelines(todos)
            case 'show':
                file = open ('todos.txt','r')
                todos = file.readlines()
                file.close()

                print ("Contents of the file include: \n")
                print(todos)
                print("Length of the contents: ", len(todos))
                for index, item in enumerate(todos):
                    nitem = item.strip()
                    print (f"{index + 1} - {nitem}")
            case 'edit':
                file = open ('todos.txt','r')
                todos = file.readlines()

                number = int(input("Number of the todo to edit: "))
                number = number -1 
                new_todo = input("Enter new todo: ") + "\n"
                #todo[number] = new_todo
                todos[number] = new_todo
                file = open ('todos.txt','w')
                file.writelines(todos)
                file.close()
            case 'complete':
                number = int(input("Number of the todo to complete: "))
                todos.pop(number - 1)
                file = open ('todos.txt','w')
                file.writelines(todos)
                file.close()                

            case 'exit' | 'quit' | 'Quit' | 'Exit':
                break
    else:
        print ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print ("          Select right option \n")
        print ("     Type add, show, edit or exit ")
        print ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

