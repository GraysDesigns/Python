# Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.
# To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.
# For example, suppose you have the following list: 
# | 1-3 a: abcde     |
# | 1-3 b: cdefg     |
# | 2-9 c: ccccccccc |
# Each line gives the password policy and then the password. 
# The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. 
# For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.
# In the above example, 2 passwords are valid. 
# The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. 
# The first and third passwords are valid: 
#   they contain one a or nine c, both within the limits of their respective policies. 



# CODE:
#define variable data as input.txt opened, read-only mode.
data = open("input.txt", "r")

array = [line for line in data.readlines()]
print (array)

# colon counter
count = 0
for i in array:
    if ':' in i:
        count += 1

print("number of colons: ", count)

