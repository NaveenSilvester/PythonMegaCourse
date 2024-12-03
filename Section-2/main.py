user_prompt = ("Enter a todo: ")

status = True
mytodo = []
while (status == True):
    user_input = input(user_prompt)
    mytodo.append(user_input.capitalize())
    if user_input == "Stop":
        status = False

print ("Here are my tasks: ", mytodo)