elements = ['a', 'b', 'c']

for index, element in enumerate(elements):
    print (index, element, sep="")


products = ['table', 'chair', 'door']

for i, product in enumerate(products):
    print (f"{i}:{product}")


filenames = ['document', 'report', 'presentation']
for index, filename in enumerate(filenames):
    print (f"{index}-{filename}.txt")



filenames = ['document', 'report', 'presentation']
for index, filename in enumerate(filenames):
    print (f"{index}-{filename.capitalize()}.txt")


mylist = ["a","b","c","d","e"]
print(mylist)
mylist.remove("e")
print(mylist)
mylist.reverse()
print(mylist)
mylist.reverse()
print(mylist)
mylist.pop()
print(mylist)