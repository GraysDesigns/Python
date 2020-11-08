# ASSIGNMENT
# -----------
# Write a Python program to compute the price of a theater ticket.
# Your program should prompt the user for the patron's age and whether the movie is 3D. 
# Children and seniors should receive a discounted price. 
# There should be a surcharge for movies that are 3D. 
# You should decide on the age cutoffs for children and seniors and the prices for the three different age groups. 
# You should also decide on the amount of the surcharge for 3D movies. 
# Your program should output the ticket price for the movie ticket based on the age entered and whether the movie is in 3D.
# -----------
# CODE
# -----------

# Define the flat ticket rate as 'ticketFlat', the surcharge for 3D movies as 'surcharge3D', and the age discount as 'ageDiscount'
ticketFlat = 8.25
surcharge3D = 3
ageDiscount = .1
# 'choice3D' is a string input as to whether or not the film is in 3D
choice3D = input('Will you be watching this film in 3D? [Y/n] \n')
# 'age' is the users age
age = eval(input('How old are you?\n'))
# This says if the choice 3D is equal to 'Y' or yes, then run lines 24-31
if choice3D == 'Y' or choice3D == 'y':
# Define ticket3D as the price of the flat ticket rate plus the surcharge
    ticket3D = ticketFlat + surcharge3D
# If the variable 'age' is less than 12, or greater than 60, then the age discount is applied in line 28
    if age < 12 or age > 60:
        ticketPrice = ticket3D - (ticket3D * ageDiscount)
# If the variable 'age' falls outside of this realm, the user is not eligable for an age-based discount
    else:
        ticketPrice = ticket3D
# This conditional runs if the user does not plan on watching a movie in 3D
else: 
# The same age conditional as before, but with the variable 'ticketFlat' instead of 'ticket3D' 
    if age < 12 or age > 60:
        ticketPrice = ticketFlat - (ticketFlat * ageDiscount)
    else:
        ticketPrice = ticketFlat    
# Finally, print the final ticket price
print ('ticket price: ' + str(ticketPrice))
