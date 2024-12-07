with open("data.txt", "r") as file:
    contents = file.readlines()
    print (contents)
    newcontents = [i.strip() for i in contents]
    print (newcontents)
    l = [int(i) for i in newcontents[1:]]
    print (l)
    a = sum(l)
    print(a)
 
def get_average(a):
    with open(a, "r") as file:
        contents = file.readlines()
        contents = [float(item.strip()) for item in contents[1:]]
        return sum(contents)/len(contents)
    

average = get_average("data.txt")
print("The average of temperatures : ", average)


def get_max():
    grades = [9.6, 9.2, 9.7]
    maximum = max(grades)
    minimum = min(grades)
    return (maximum, minimum)

(a,b) = get_max()    
print(f"Max: {a}, Min: {b}")


def format_filename():
    filename = "report.txt"
    filename = (filename[:-4]).capitalize()
    return(filename)  

print(format_filename())
