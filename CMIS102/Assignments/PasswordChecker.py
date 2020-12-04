## Assignment
# ----------
# [x] The fifth assignment involves writing a Python program to determine whether a password meets all the    requirements for a secure password. 
# [x] Your program should prompt the user for the candidate password and 
# [x] output either that the password is valid 
# [x] or the reason it is invalid. 
# [x] To be valid the length of the password must greater than some minimum length 
# [x] but less than some maximum. 
# [x] It must not include the substring "umgc" 
# [x] in any combination of upper or lower case letters. 
# [x] Finally, it must contain the # symbol 
# [x] in some position other than the first or last character. 
# [x] You should decide on the minimum and maximum allowable lengths.

password = input('Please enter a password:\n')
errors = []
valid = True


# Checks if the length of the password is within the bounds of the character minimum and limit
def length(var):
# if the length is more than 8 characters, but less than 20, it falls withing normal parameters. Return True
    if len(var) >= 8 and len(var) < 20:
        return True
# otherwise, if it is less than 8 characters, return a string saying why it's invalid
    elif len(var) < 8:
        return "Password must be 8 characters or more"
# otherwise, if it is more than 20 characters, return a string saying why it's invalid
    else:
        return "Password must be less than 20 characters" 

# Checks if the # symbol is in the password and not the first or last character
def hash(var):
# if the # symbol is withing the bounds of the first and last symbol, return True
    if '#' in var[0] or '#' in var[len(var) - 1]:
        return "'#' symbol may not be the first or last character of your password"
# if the # symbol is the first or last symbol, return a string saying why it's invalid
    elif '#' in var[1:(len(var) - 2)]:
        return True
# if the string does not include the # symbol, return a string saying why it's invalid
    else: 
        return "Password must include the '#' symbol"    



# checks if the substring 'umgc' in any case is in the password
def word(var):
# turn all the letters into lowercase 
    lower = str.lower(var)
# if 'umgc' is a substring of the password, return a string saying why it's invalid
    if 'umgc' in lower:
        return "Password may not contain the characters 'UMGC' in any form"
# otherwise return True 
    else: 
        return True


# if the length(password) is not true, it sets the variable 'valid' to False, so the code on line 69 does not run and the user doesn't get an erroneous success message.
if length(password) != True:
    valid = False
# add the error message returned from the function length() to the errors array
    errors.append(length(password))

# repeat this process for the other errors
if hash(password) != True:
    valid = False
    errors.append(hash(password))

if word(password) != True:
    valid = False
    errors.append(word(password))

# if valid is True, then print that the password inputed is a valid password
if valid:
    print(password + " is a valid password!!")

# for loop iterates the elements of the errors[] array to give user reasons why their password is invalid
for error in errors:
    print(error)


# Tests:
# hash True, word True, length False (<8) '2#34'
# hash False(in first and last), word True, length False (>20) '#####################'
# hash False(in first), word False (umgc), length False (<8) '#umgc'
# hash False(none), word False(uMgC), length True 'uMgC202020'
# hash True, word True, length True (<8) '2#wwwaaa'




