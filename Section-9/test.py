'''
a = input("Enter the password")
if len(a) > 7:
    print ("Great Passwod there!")
'''


password = input("Enter a password: \n")
if len(password) > 7:
    print ("Great Password there!")
elif len(password) == 7:
    print ("Password is Ok")
elif len(password) < 7:
    print ("Your password is weak")


day_temperatures = {
    'morning' : ("Good", "Morning"),
    'noon' : ("Good", "Afternoon"),
    'evening' : ("Good", "Evening")
}

#day_temperatures = {'morning': 6.0, 'noon' : 12.0, 'evening': 4.0}

for key, value in day_temperatures.items():
    print (key, value)