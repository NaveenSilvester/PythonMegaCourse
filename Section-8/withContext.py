with open ("WithContext.txt", "w") as file:
    file.write("This is the text that I want to enter into this file.")

with open ("WithContext.txt", "r") as file:
    print (file.read())


    