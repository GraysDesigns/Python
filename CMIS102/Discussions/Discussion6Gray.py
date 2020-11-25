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

def hasSpace(string):
    count = 0
    for space in word:
        if space == ' ':
            count +=1
    if count > 0:
        return True
    else:
        return False

word = input("What is your favorite word?\n")
print(hasSpace(word))

if hasSpace(word) == False:
# print the length of the inputted string
    print(word, "is", str(len(word)), "letters long")
# print a phrase showing what the program is doing
    print("Here's how you spell", word)

# start counter at 0
    i = 0
# starts the count at 0, and prints the letter of that index of the string
    while i < len(word):
        letter = word[i]
        print (letter)
# iterate the variable 1 to move on to the next index of the string.
        i += 1
else:
    print("Please enter a valid word, not a phrase")
