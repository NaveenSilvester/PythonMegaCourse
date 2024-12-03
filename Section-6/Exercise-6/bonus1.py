files = ["FirsFile.txt", "SecondFile.txt", "ThirdFile.txt"]
contents = ["MyFirst Text file", "MySecond Text File", "MyThird Text File"]


for index, file in enumerate(files):
    file = open (file, "w")
    print(contents[index])
    file.writelines(contents[index])
    file.close()


