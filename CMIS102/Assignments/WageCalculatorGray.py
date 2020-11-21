# ASSIGNMENT
# -----------
# The first assignment involves writing a Python program to compute the weekly pay for a salesman. 
# 
# Your program should prompt the user for the number of hours worked for that week and the weekly sales. 
# 
# Your program should compute the total pay as the sum of the pay based on the number of hours worked times the hourly rate plus the commission. 
# 
# You should chose a value for the hourly pay. 
# 
# The commission should be computed as a percentage of the weekly sales. 
#
# You should choose a value for the percentage. 
# 
# Your program should output the pay based on the hours worked, the commission and the total pay for the week.


# CODE
# ----

# User inputs the number of hours they've worked.
hours = int(input('How many hours have you worked this week: '))

# User inputs the number of sales they made.
salestotal = int(input('How many sales did you make this week: '))

# Program defines the hourly wage of the salesperson and their commission percentage. Both of which can be changed later by management.
rate = 15
commissionpercent = 0.2

# Program then computes the wage from commission.
commission = (commissionpercent * salestotal)

# Finally, the program computes the final pay of the user based on (the hours they've worked * their rate) + their commission total.
pay = (hours * rate) + commission

# User sees hours * rate value, assuming hours worked is less than 40. 
if hours <= 40:
    print("You've worked: " + str(hours) + " hours this week at a rate of " + str(rate) + "$ per hour.")
    # Comissionpercent is multiplied by 100 for readability by the user.
    print("You made: " + str(salestotal) + " sales, and our company commission rate is " + str(100 * commissionpercent) + "%. This brings the total you made on commission this week: " + str(commission) + "$")
    # Final total
    print("Your total pay this week before taxes is: $" + str(pay) + ". Thank you!")
else:
    print('It seems you\'ve worked overtime this week, please see your supervisor for further guidance.')


