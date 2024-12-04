prompt = input("Enter today's date: \n")
filename = prompt+".txt"
exercise = input("How many minutes you spent on exercise: \n") + "\n"
mood = input("Let your thoughts flow about the day: \n") + "\n"

with open(filename, "w") as file:
    file.write(exercise)
    file.write(mood)
print("Printing the contents of the file\n")
with open(filename, 'r') as file:
    print (file.read())04-12-2020