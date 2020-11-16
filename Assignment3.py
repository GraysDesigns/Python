# Assignment
# -----------
# Write a Python program to compute the cost of carpeting a room. 
# Prompt the user for the width and height in feet of the room and the quality of carpet to be used. 
# A choice between three grades of carpeting should be given. You should decide on the price per square foot of the three grades on carpet. 
# Your program must include a function that accepts the height, width, and carpet quality as parameters and returns the cost of carpeting that room. 
# After calling that function, your program should then output the carpeting cost.
# -----------
# CODE
# -----------

# User inputs length and width as integers, and the quality of carpet they'd like to use as a string
length = eval(input("What is the length of space in feet? \n"))
width = eval(input("What is the width of space in feet? \n"))
qual = input("Which Quality of carpet would you like? (ex. Economy, Midgrade, Luxury)\n")

# The function qualCost() takes the string input from the user and converts it into the price per square foot of carpeting, this becomes a multiplier later on. You can see that there are many "or" functions to accomidate for various kinds of inputs that are outside the realm of the example
def qualCost(q):
# if the user selects the economy grade carpet, the price is $0.70/sqft
    if q == "economy" or q == "Economy" or q == "econ":
        return .7
# if the user selects the midgrade carpet, the price is $1.50/sqft
    elif q == "Midgrade" or q == "midgrade" or q =="mid":
        return 1.5
# if the user selects the midgrade carpet, the price is $2.10/sqft
    elif q == "Luxury" or q == "luxury" or q == "lux":
        return 2.1   
# NOTE: dollar amounts/sqft of carpet are taken from current lowes pricing


# Next we create a sqft() definition, sqft() takes two parameters (length and width) and multiplies them to get the total square footage of the area to be covered by carpet
def sqft(l, w):
    return (l*w)

# The Dollar() function says if the dollar amount passed in is a whole number (modulus 0 i.e. no remainder) then it returns an integer with no float, otherwise, the cost is rounded to the nearest hundredth decimal place, as is how monetary values are usually given. 
def Dollar(d):
    if d % 1 == 0:
        return int(d)
    else:
        return round(d, 2)    

# This is our total cost function. It takes the Dollar function and passes through the square footage function (sqft()) and multiplies it by the qualCost() function to get the total price of the carpet to be sold. 

totalCost = Dollar((sqft(length, width) * qualCost(qual)))

# The functions then need to be passed as strings to be printable
print ("You are buying " + str(sqft(length, width)) + " sq.ft. of carpet at $" + str(Dollar(qualCost(qual))) + " per sq.ft.")

print ("Your total cost today is $" + str(totalCost))