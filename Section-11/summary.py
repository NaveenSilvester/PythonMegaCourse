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
        contents = [int(item.strip()) for item in contents[1:]]
        return sum(contents)/len(contents)
    

average = get_average("data.txt")
print("The average of temperatures : ", average)
