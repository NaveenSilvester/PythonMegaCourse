filenames = ["1.doc", "1.report", "1.presentation"]
# Output expected: newfiles = ["1-doc.txt","1-report.txt", "1-presentation.txt"]

newfiles = [ item.replace('.','-')+".txt" for item in filenames]
print (newfiles)


names = ["john smith", "jay santi", "eva kuki"]
names = [name.title() for name in names]
print (names)

temperatures = [10, 12, 14]
temperatures = [str(item)+"\n" for item in temperatures]
print(temperatures)
file = open("file.txt", 'w')
file.writelines(temperatures)

my_list = ['apple', 'banana', 'cherry', 'date']
my_dict = { item:len(item) for item in my_list }
print (my_dict)


keys = ['name', 'age', 'city']
values = ['John', 25, 'New York']

my_contact = {keys[i]:values[i] for i in range(len(keys))}
print (my_contact)

old = [1,2,3]
new = [ i + 10 for i in old ]
print(new)


word = "Python"
vowels = "aeiou"

# find vowel in the string "Python"
result = [char for char in word if char in vowels]

print(result)



# Nested list comprehension
matrix = [[j for j in range(6)] for i in range(4)]
 
print(matrix)


# Nested list comprehension
matrix = [["apple", "banana", "cherry"],
		["date", "fig", "grape"],
		["kiwi", "lemon", "mango"]]

modified_matrix = [[fruit.capitalize() for fruit in row] for row in matrix]

print(modified_matrix)


new = [ [row  for row in ["A","B","C"]] for row in range(4)]
print (new)



char = ["X","Y","Z"]
new = [ [char[row]  for i, c in enumerate(char)] for row in range(3)]
print(new)


matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flatten_matrix = [val for sublist in matrix for val in sublist]
print (flatten_matrix)

# get odd numbers
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
odd = [ i for sublist in matrix for i in sublist if i%2 != 0]
print (odd)
