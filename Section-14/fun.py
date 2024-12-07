def area(side):
    """
    This is a function that calculates the area of a square given the length of the side
    """
    return (side * side)

def calculate_time(h,g=9.80665):
    t = (2 * h / g) ** 0.5
    return t

#print(area(2))
print(f"Module {__name__} is loaded")
if __name__ == "__main__":
    print ("Hi, I am inside the module, executed only when I am run as a module file 'fun.py'")