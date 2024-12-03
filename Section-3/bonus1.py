todos = []

while True:
    user_action = input("Type add or show or quit: ")

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            print(todos)
        case 'quit':
            print ("Thank you!")
            break
print ("Bye for Now!")



while True:
    country = input("Enter the name of the country: ")
    
    match country:
        case 'Italy':
            print ("Ciao its Italy")
        case 'USA':
            print ("Hello its USA")
        case 'Germany':
            print ("Hallo its Germany")
        case 'Quit':
            break

print ("Thank you for using my App")


while True:
    country = input("Enter the name of the country: ")
    match country:
        case "Italy":
            print ("Halo I am in Italy")
        case "USA" | "United States":
            print ("Hello I am in  States")
        case "Quit" | "quit" | "exit":
            print ("I am done!")
            break