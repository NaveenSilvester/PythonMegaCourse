def get_nr_items(user_input):
    myitems = user_input.split(",")
    return (len(myitems))

print (get_nr_items("john,list,teresa"))


def areaOfSquare(side):
    return (side * side)
    
print (areaOfSquare(7))


def weather(temp):
    #today = "Warm" if temp > 7 else "Cold"
    #return(today)
    return ("Warm" if temp > 7 else "Cold")

print (weather(4))


def lenstr (string):
    return ("False" if len(string) < 8 else "True")

print (lenstr("Naveen Silvester"))
print (lenstr("Allen"))



def calculate_time(h,g=9.80665):
    t = (2 * h / g) ** 0.5
    return t
      
time = calculate_time(h=100,)
print(time)