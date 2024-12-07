liters = int(input("To convert Liters to Cubic Centimeter, enter value in Liters: \n"))

def liters_to_m3 (liters):
    cubic_meters = liters * 1000
    return (cubic_meters)
    
print (f"{liters} liter is equal to {liters_to_m3(liters)} cubic centimeters")