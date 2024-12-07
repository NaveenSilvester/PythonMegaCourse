feet_inches = input("Enter Feet and Inches: \n")

def convert(feet_inches):
    (ft,inch) = feet_inches.split(" ")
    ft_meters = float(ft) *  304.8
    inch_meters = float(inch) * 25.4
    meters = (ft_meters + inch_meters)/1000
    #return (f"Feet {ft} and Inches {inch} in Meters is {meters} meters")
    return (meters)


def report ():
    meters = convert(feet_inches)
    if meters < 1:
        report = ("The hight is less than a meter\n")
    else:
        report = ("The height is Greater than 1 meter")
    return(report)


print (convert(feet_inches))
print(report())