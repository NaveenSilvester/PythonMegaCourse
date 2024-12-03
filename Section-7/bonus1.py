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