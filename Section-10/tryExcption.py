try:
    # Example of ZeroDivisionError
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

try:
    # Example of FileNotFoundError
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")

try:
    # Example of ValueError
    number = int("not_a_number")
except ValueError:
    print("Invalid value!")
