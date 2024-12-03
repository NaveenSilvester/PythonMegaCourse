"""
This program takes entry of a new member to the file neamed members.txt 
To exit the program the user need to type Q or q

"""


while True:
    prompt = input(
    '''Wanted to add a New Member?  
       (Note:To Quit app, type Q or q)
Enter the name of the new member: \n''') + "\n"
    if prompt in ['Q\n', 'q\n']:
        exit()
    else:
        members = open('members.txt', 'r')
        all = members.readlines()
        print (type(all))
        all.append(prompt)
        members.close()
        print(all)

        members = open('members.txt', 'w')
        members.writelines(all)
        members.close()   
    


