## Assignment
# ----------
#[x] Post a Python program that accepts a string as input. 
#[x] It should analyze some characteristic of that string and 
#[x] display the result of that analysis. 
#[x] The program must use at least one of the following: 
#[ ]    string slices
#[x]    string conditions
#[ ]    string methods

# ----------
# CODE
# ----------


# define a function that will count, but only if the input has no space
def counter(w):
    # call a function hasSpace() that is defined on line 26
    if hasSpace(w) == False:
        # print the length of the inputted string
        print(w, "is", str(len(w)), "letters long")
        # run the function howSpell() that is defined on line 43
        howSpell(w)


def hasSpace(string):
    # returns boolean True or False if string has space using a simple iterator detection loop
    # start the count at 0
    count = 0
    # iterate through the characters in the functions input of string
    for char in string:
        # if the current string that the for loop is iterating on is a space, the counter ticks one
        if char == ' ':
            count +=1
    # if the counter is greater than 0, it means that the for loop on line 30 has found a space, thus the function should return a boolean value of True       
    if count > 0:
        return True
    # if the count is 0, then the for loop has found no spaces, the function returns boolean False
    else:
        return False


def howSpell(word):
    # print a phrase showing what the program is going to do, which is spell the input
    print("Here's how you spell", word)
    # start counter at 0
    i = 0
    # starts the count at 0, and prints the letter of that index of the string
    while i < len(word):
        letter = word[i]
        print (letter)
        # iterate the variable 1 to move on to the next index of the string.
        i += 1

# ask user what their favorite word is, store that value in the variable 'word'
word = input("What is your favorite word?\n")

# run the user input 'word' through the hasSpace function (line 26), if the input has a space, it is a phrase and not a word, so it will not be spelled
while hasSpace(word) == True:
    # This while loop will run indefinitely until the userinput contains no spaces. 
    word = input("Please enter a valid word, not a phrase\n")

# finally, if the input passes the test on line 59 and has no spaces, then move call the counter() function defined on line 17
counter(word)