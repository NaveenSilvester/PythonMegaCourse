password = input("Enter your password here: \n")


def check_password_policy(password): 
    has_len = False
    has_char = False
    has_upper = False 
    has_num = False
    plen = 0
    pc = 0
    pcu = 0
    pn = 0 
    pnc = 0
    
    if (len(password) > 8):
        has_len = True
        plen = 1
    
    for char in password: 
        if char.isalpha(): # Checks if the character is char datatype
            has_char = True
            pc = 1
        if char.isupper(): # Checks if the character is a upper case
            has_upper = True
            pcu = 1 
        if char.isdigit(): # Checks if the character is a digit
            has_num = True
            pn = 1 
        if char.isalnum() == False: # Checks if the character is a non alpha numeric
            pnc = 1

    rep = [plen, pc, pcu, pn, pnc] # A digital signature of password
    return (rep)



def report(password):
    print ("This is :", check_password_policy(password))
    if (sum(check_password_policy(password)) > 3):
#        print (f"The password {password} is a Strong Password which is compliant to the Password Policy {check_password_policy(password)}\n")
        return (f"The password {password} is a Strong Password which is compliant to the Password Policy {check_password_policy(password)}\n")
    elif (sum(check_password_policy(password)) <= 3 and sum(check_password_policy(password)) > 1):
#        print (f"The password {password} is a Weak Password as per the Password Policy {check_password_policy(password)}\n")
        return (f"The password {password} is a Weak Password as per the Password Policy {check_password_policy(password)}\n")
    else:
#        print (f"The password {password} is non compliant to the Password Policy {check_password_policy(password)}\n")
        return (f"The password {password} is non compliant to the Password Policy {check_password_policy(password)}\n")
  

print (f"Password {password} character {check_password_policy(password)}" )
print (f"Thi report is {report(password)}")

'''

onlyAlpha = password.isalpha()
#print (onlyAlpha)

onlyDigit = password.isdigit()
#print(onlyDigit)

alphaNum = password.isalnum()
#print (alphaNum)


def lenght(password):
    plength  = len(password)
    if plength > 8:
        p = "Y"
        return (p)
    else:
        p = "N"
    return(p)


def alphanum(password):
    alphanum = password.isalnum()
    return (alphanum)

def onlyDigit(password):
    onlyDigit = password.isdigit()
    return (onlyDigit)

def upper(password):
    up = "False"
    if (onlyDigit(password) == False):
        for char in password:
            if char.isupper() == True:
                up = "True"
                return (up)
                break
            else:
                up = "False"
    return(up)

'''
