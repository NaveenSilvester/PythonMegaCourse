file = open ('members.txt', 'r')
mytext = file.readlines()
print ("Original file contents are: ", mytext)
file.close()
#contents = [ item.strip("\n") for item in mytext if len(item) <4 ]
contents = [ item for item in mytext if len(item) > 5]

print ("The new file contents names of members whose lenght is >5 are:  ", contents)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
even_numbers = [num for num in numbers if num % 2 == 0] 
print(even_numbers)

