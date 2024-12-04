
try:
    number = int(input("Enter a number: \n"))
    print ("the number is ",number)
except ValueError:
    print("Please enter a valid number")
    number = int(input("Enter a number: \n"))  