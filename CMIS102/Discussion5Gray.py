# Assignment
# ----------
# Post a Python program that contains a while loop. 
# The number of times the loop iterates should depend upon input supplied by the user. 
# Your program should display some output each time the loop executes. 

# CODE (roll initiative)
# ---------

# import the random module
import random

# define the function roll20() to return a random integer from 1 - 20 to simulate a 20 sided die
def roll20():
    return random.randint(1,20)

# prompt user how many members are in their party
playersNumber = eval(input("How many members are in your party?\n"))

# define empty player's array
playersArray = []
# Start count at 1, this will make asking the user for the player's names easier
count = 1
# prompt user for all the member's names
while playersNumber > (count - 1):
    playersArray.append(input("Player " + str(count) + " name: "))
    count += 1
# define an empty array for player's initiative
initiative = []
# run rol20() once every time there is a player in playersArray
for i in playersArray:
    initiative.append(roll20())

# final print statement. For every player in the array, it displays their initiative roll. 
count = 0
for i in playersArray:
    print(i + "'s roll: " + str(initiative[count]))
    count += 1







