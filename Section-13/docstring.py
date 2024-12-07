password = input("Enter your password here: \n")



def generate_password_signature(password):

    """
        Reads a user entered password and then checks for its password compliance
        and prints a digital signature for the password
    """
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
#print(help(generate_password_signature ))

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
    