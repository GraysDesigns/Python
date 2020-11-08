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
# The current month is logged as todayMonth.
todayMonth = today.month
# Asks the user what year they were born in. Type is an integer denoted by 'int' at the end of the variable.
birthYearint = int(input('What year were you born?\n'))
# Asks the user what month they were born in, expected input to be full spelled out names of the month. 
# For now, input is currently a string denoted by 'str' at the end of the variable. 
birthMonthstr = input('What month were you born?\n')
# Using the previous data, asks the user what day of the month they were born. Type is an integer denoted by 'int' at the end of the variable.
birthDayint = int(input('What day of ' + birthMonthstr + ' were you born on?\n'))
# Using the 'strptime' module, we take the spelled out month, annotated by the '%B' and convert it into datetime syntax. Now the variable can be used as an integer as denoted by the 'int' at the end of the variable.  
birthMonthint = dt.datetime.strptime(birthMonthstr, '%B').month
# Now we aggregate the previous variables to get our full date of the users birthday in the datetime format. 
birthdayFull = dt.date(birthYearint, birthMonthint, birthDayint)
# Using the previous data, we find the users birthday of this year
thisYearBirthday = dt.date(today.year, birthMonthint, birthDayint)
# This is the same variable as the last, except for next year. This is used if the users birthday has already passed (see line ##)
nextYearBirthday = dt.date(today.year +1, birthMonthint, birthDayint)
# This is the difference in days until or since the users birthday. 
delta = (thisYearBirthday - today)
days = delta.days
age = today.year - birthYearint

if days == 0:
    print('it\'s your birthday! You are ' + str(age) + ' years old. Happy birthday!!')
elif days > 0:
    print ('There are ' + str(days) + ' until your birthday. You will be ' + str(age) + ' years old.')
else:
    print ('Your birthday is coming up')
