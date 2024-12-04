
######################################################################################################
try:
    width = float(input("Enter the value of the width: \n"))
    length = float(input("Enter the value of the length: \n"))
    area = width * length
    print(f"Area of the rectangle with {width} and {length} is {area}")
except ValueError:
    print ("Please Enter a Number")
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

######################################################################################################
try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    print ("This is ", (value/total_value)*100, "%")
except ValueError:
    print ("You need to enter a number. Run the Program again.")
except ZeroDivisionError:
    print ("Your Total Value cannot be equal to Zero, enter correct total value")
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%   

######################################################################################################
filenames = ["report.txt", "downloads.txt", "success.txt", "folders.txt"]
for file in filenames:
    print (file[:-4])
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

######################################################################################################
filenames = ["report.txt", "downloads.txt", "success.txt", "folders.txt"]
for file in filenames:
    print (file[:-4].capitalize())

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

######################################################################################################
waiting_list = ["john", "marry"]
name = input("Enter name: ")
 
#number = waiting_list.index(name)
print(waiting_list.index(name))
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%




