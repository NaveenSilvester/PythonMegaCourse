password = input('''
##################################################################################################################################
                Password Strength idenfier app
The password must contain minumum of 4 characters, and aleast one uppercase and one numeric. Non Alpha characters are not allowed.
##################################################################################################################################
Kindly Enter your password: \n''')

length = len(password)

upper = False
onlyAlpha = password.isalpha()
#print (onlyAlpha)

onlyDigit = password.isdigit()
#print(onlyDigit)

alphaNum = password.isalnum()
#print (alphaNum)

if onlyAlpha == True or onlyDigit == True or alphaNum == False or length < 5:
     if onlyAlpha == True:
           print ("Note:\nPassword only contains Alphabets and no Numeric content in it, do include digits")
     elif onlyDigit == True:
           print ("Note:\nPassword only contains digits and no alphabets, kindly include alphabets")
     elif alphaNum == False:
           print ("Note:\nThe password contains non alphanumeric characters")
     elif length < 5:
           print (f"Note:\nThe length of the password is {length} which lesser than minimum 5 characters")        
elif alphaNum == True and upper == False:
    for char in password:
          upper = char.isupper()
          print (f"SUCCESS: Its a great strong password {password}")
          break
else:
	print ("Note:\n The password did not meet the criteria defined")
