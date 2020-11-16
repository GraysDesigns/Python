# Assignment
# -----------
# Post a Python program that accepts at least three values as input, 
# performs some computation and displays at least two values as the result. 
# The program must include an if statement that performs 
# different computations based on the value of one of the inputs. 
# Include comments in your program that describe what the program does. 
# Also post a screen shot of executing your program on at least two test cases.
# -----------
# DESCRIPTION
# The following program asks for your birthday, and from the current day calculates how many days it is until your birthday, it also outputs how old you will be on your birthday
# If it is your birthday, the program outputs 'Happy Birthday!'
# -----------
# CODE
# -----------

# First we need to import the datetime module to be able to work with dates and times, we also shorthand it to 'dt' so that we avoid repeating the phrase 'datetime'
import datetime as dt

# set the variable 'today' equal to the current date in the datetime module.
today = dt.date.today()

# To test various dates and cases, comment the line above (^) and uncomment the line below (v), the format is (YYYY, M, D) You can then input any day to test whether the program works
###today = dt.date(2020, 1, 14)###

# The current month is logged as todayMonth.
todayMonth = today.month
# The current year is logged as todayYear.
todayYear = today.year 

# nextLeapyearBool uses the modulus calculation to either be boolean statements of 'True' of 'False' which say whether or not this year or next year are leapyears respectively.
nextLeapyearBool = (today.year + 1) % 4 == 0

# Asks the user what year they were born in. Type is an integer denoted by 'int' at the end of the variable.
birthYearint = int(input('What year were you born?\n'))

# Asks the user what month they were born in, expected input to be full spelled out names of the month. 
# For now, input is currently a string denoted by 'str' at the end of the variable. 
birthMonthstr = input('What month were you born? (ex. november)\n')

# Using the previous data, asks the user what day of the month they were born. Type is an integer denoted by 'int' at the end of the variable.
birthDayint = int(input('What day of ' + birthMonthstr + ' were you born on?\n'))

# Using the 'strptime' module, we take the spelled out month, annotated by the '%B' and convert it into datetime syntax. Now the variable can be used as an integer as denoted by the 'int' at the end of the variable.  
birthMonthint = dt.datetime.strptime(birthMonthstr, '%B').month

# Using the previous data, we find the users birthday of this year
thisYearBirthday = dt.date(today.year, birthMonthint, birthDayint)

# This is the difference in days until or since the users birthday. 
delta = (thisYearBirthday - today)

# The 'days' variable strips the delta down to how many days it is equal to
days = delta.days

# The users age is equal to the current year minus the year they were born. ex. 2020 - 1998 = 22; the user is 22 years old.
age = today.year - birthYearint

# if the variable 'days' is equal to 0, this means that the users birthday is today. 
if days == 0:
    print('it\'s your birthday! You are ' + str(age) + ' years old. Happy birthday!!')

# Otherwise, if the variable 'days' is greater than 0, that means their birthday has not passed yet this year.   
elif days > 0:
# This passes the amount of days left until their birthday.
    print ('There are ' + str(days) + ' days until your birthday. You will be ' + str(age) + ' years old.')
# If the variable 'days' is not 0, nor is it greater than 0, it must be a negative number, meaning their birthday has already passed this year. 

# Since days is negative and nextLeapyearBool is false, i.e. the next year only has 365 days we continue with this elif statement.
elif days < 0 and nextLeapyearBool == False:
# This prints the absolute value of the days until the users next birthday, since here 'days' is negative, we must add days to get to the positive number
# This also prints 'age + 1' since the users birthday has already passed this year and 'age' only presents the users age for the current year. 
# Note: since 'today' has technically already passed, we add 364 to the days variable to get the number of days until the users birthday. 
    print ('Your birthday is in ' + str(abs(364 + days)) + ' days. You will be ' + str(age + 1) + ' years old.')

# Otherwise, the next year is a leapyear, and 365 days should be added instead of 364.
else:
    print ('Your birthday is in ' + str(abs(365 + days)) + ' days. You will be ' + str(age + 1) + ' years old.')  
