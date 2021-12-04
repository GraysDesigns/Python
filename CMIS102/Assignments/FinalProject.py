# Assignment
# ----------
# The final project involves writing a Python program to determine the body-mass index of a collection of six individuals. 
# [x] Your program should include a list of six names. 
# [x] Using a for loop, it should successively 
# [x] prompt the user for 
#   [x] the height in inches and 
#   [x] weight in pounds of each individual. 
# [x] Each prompt should include the name of the individual whose height and weight is to be input. 
# [x] It should call a function that accepts 
#   [x] the height and 
#   [x] weight as parameters and 
#   [x] returns the body mass index for that individual using the formula weight × 703 / height^2. 
# [x] That body mass index should then be appended to an array. 
# [ ] Using a second loop it should 
#   [ ] traverse the array of body mass indices and 
#   [ ] call another function that 
#       [x] accepts the body mass index as a parameter and 
#       [x] returns whether the individual is underweight, normal weight or overweight. 
# [ ] The number of individuals in each category should be counted and 
# [ ] the number in each of those categories should be displayed. 
# [x] You should decide on the names of the six individuals and the thresholds used for categorization.
# ---------
# NOTES 
# ---------
# BMI Equation: weight(lbs) * 703 / height(in) ^2
# BMI Thresholds:
# Underweight: ( ,18.5) 
# Normal weight: [18.5, 25)
# Overwieght: [25, 30)
# ---------
# CODE 
# ---------

# define names array 
names = ["Jennifer", "Tanya", "Bryan", "Hannah", "Alicia", "William"]
# define empty arrays for weights, heights, and BMIs
weights = []
heights = []
bmis = []
# define zeros for underweight, normal weight, and overweight counters 
underweight = 0
normalweight = 0
overweight = 0
# define bmi function that takes weight and height as parameters, and using the bmi equation returns their BMIs
def bmi(weight, height):
    return ((weight * 703) /(height ** 2))

# define bmi classifier
def bmiClass(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    else:
        return "Overweight"

# Prompt user for everyone in the list's weight and height, append those values to the empty arrays defined before
for name in names:
    weights.append(eval(input("What is " + name + "'s weight in pounds? ")))
    heights.append(eval(input("What is " + name + "'s height in inches? ")))

# Start iterator at 0
i = 0
# as long as the iterator is less than the length of the weights, execute the code inside
while i < len(weights):
# append the the empty BMI array the returned value of the previously defined BMI function using the current iteration as indexes of the array
    bmis.append(bmi(weights[i], heights[i]))
# increase iterator +1
    i += 1

# loop through the bmis in the bmi array
for bmi in bmis:
# if the bmiClass() function returned "underweight", iterate the underweight counter +1
    if bmiClass(bmi) == "Underweight":
        underweight += 1
# if the bmiClass() function returned "normal weight", iterate the normalweight category +1
    elif bmiClass(bmi) == "Normal weight":
        normalweight += 1
# otherwise, iterate the overweight counter + 1
    else:
        overweight += 1

print ("There are", str(underweight), "underweight individuals in this group.")
print ("There are", str(normalweight), "individuals of normal weight in this group.")
print ("There are", str(overweight), "overweight individuals in this group")