user_prompt= ("Enter the Title: ")

my_titles = []
while True:
    user_input = input(user_prompt)
    print (user_input.title())
    my_titles.append(user_input.title())
    print (my_titles)

