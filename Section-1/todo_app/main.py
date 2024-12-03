user_prompt = "Enter a todo:"
#user_input = input(user_prompt)
#print (user_input)

mytodos = []
for i in range(3):
    user_input = input(user_prompt)
    print (user_input)
    mytodos.append(user_input)

print (mytodos)


user_title_prompt = ("Enter the Title: ")
user_title =  input(user_title_prompt)
print ("Title Length is : ", len(user_title))
