filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

i=0
for filename in filenames:
    print (filename)
    s = filename.replace(".","-",1)
    print (s)
    filenames[i] = s
    print (filenames)
    

