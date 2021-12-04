# Assignment
# -----------
# The sixth assignment involves writing a Python program to 
# [x] read in the temperatures for ten consecutive days in Celsius and
# [x] store them into an array. 
# [x] The entire array should then be displayed. 
# [x] Next each temperature in the array should be converted to Fahrenheit and 
# [x] the entire array should again be displayed. 
# [x] Finally, the number of cool, warm and hot days should be counted and 
# [x] the number of each type of days should be displayed. 
# [x] You should decide on the thresholds for determining whether a day is cool, warm or hot.
### The formula for converting Celsius to Fahrenheit is °F = (°C × 1.8) + 32. ###
# -----------
# CODE
# -----------

tempsC = []
tempsF = []
coolDays = 0
warmDays = 0
hotDays = 0

for i in range (10):
    tempsC.append(eval(input("Please enter temperature number " + str(i+1) + " in Celsius: ")))

print('The temperatures in celsius have been:')
for i in tempsC:
    print (str(i) + 'C')

for i in tempsC:
    tempsF.append((i * 1.8) + 32)

print("The temperatures in fahrenheit have been:")
for i in tempsF:
    print (str(i) + 'F')

for i in tempsF:
    if i <= 69:
        coolDays +=1
    elif i <= 85:
        warmDays += 1
    else:
        hotDays += 1     

print("The number of Cool days has been: ", str(coolDays))
print("The number of Warm days has been: ", str(warmDays))
print("The number of Hot days has been: ", str(hotDays))