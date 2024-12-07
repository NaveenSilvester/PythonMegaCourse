password = input("Enter your password here: \n")

'''
num_char = [ char.isalpha() for char in password  ]
print (num_char)
print (f"Number of Characters is : ", {sum(num_char)})

num_upperchar = [ char.isupper() for char in password  ]
print (num_upperchar)
print (f"The number of Uppercase Characters : ", sum(num_upperchar))

num_digit = [char.isdigit() for char in password]
print (num_digit)
print (sum(num_digit))
print (f"Number of digits in the password : ", sum(num_digit))

num_nonalphanumeric = [char.isalnum() for char in password]
print (num_nonalphanumeric)
len_pw = len(password)
print (len_pw - sum(num_nonalphanumeric) )
print ("Number of nonAlphaNumeric Characters : ", (len_pw - sum(num_nonalphanumeric)))
'''

def generate_password_signature(password):
    signature = []
    num_char = sum([ char.isalpha() for char in password  ])
    num_upperchar = sum([ char.isupper() for char in password  ])

    num_digit = sum([char.isdigit() for char in password])

    num_nonalphanumeric = [char.isalnum() for char in password]

    len_pw = len(password)

    num_nonnc = (len_pw - sum(num_nonalphanumeric))

    signature.append(len_pw)
    signature.append(num_char)
    signature.append(num_upperchar)
    signature.append(num_digit)
    signature.append(num_nonnc)
    return (signature)

#print (generate_password_signature(password))

def generate_report (password):
#    mysignature = generate_password_signature(password)
#    password_policy = [ 1 for i in mysignature if i > 0] 
    # Setting Password Length threshold 
    minimum_password_len = 8
    maximum_password_len = 15
    mysignature = generate_password_signature(password)

#    print (f"HERE IS Digital Signarure of password {mysignature} and Len is {mysignature[0]}")
    if mysignature[0] < minimum_password_len or mysignature[0] > maximum_password_len :
        return ("Note: The length of the password should be more than 7 and less than 15")
    if mysignature[0] > minimum_password_len and mysignature[0] < maximum_password_len :
        
        # Categorizing Weak Password and Strong Password
        # Weak Password is where 3 of the 5 policy is met : 
        #    1. Minumum Length
        #    2. Contains atleast one Alphabet
        #    3. Contains atleast one Uppercase alphabet
        #    4. Contains atleaast one Digit
        #    5. Contains atleast one Non Alpha Numeric Character
        
        password_policy = [ 1 for i in mysignature if i > 0] 
#        (password_policy_report) = (mysignature, password_policy)

        if (sum(password_policy) == 5):
            return (f"Password is a Strong Password with Signature {mysignature} and policy {password_policy} and {sum(password_policy)} ")
        if (sum(password_policy) >= 3 and sum(password_policy) < 5):
            return (f"Password is a Weak Password with Signature {mysignature} and policy {password_policy} and {sum(password_policy)} ")
        if (sum(password_policy) < 3):
            return(f"The password only satisfy {password_policy} and {sum(password_policy)} category of the 5 compliance category")

print (generate_report(password))    
    
    

'''
def check_password_policy(password): 
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