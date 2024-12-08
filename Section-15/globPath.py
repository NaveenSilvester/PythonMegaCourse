import glob
r = glob.glob('./*.py')
print(len(r))

for file in r:
    print (file)