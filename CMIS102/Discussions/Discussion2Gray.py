# Assignment
# ----------
# Post a Python program that accepts:
# 
# at least two values as input, 
# performs some computation 
# displays at least one value as the result. 
# Include comments in your program that describe what the program does.
# Also post a screen shot of executing your program on at least one test case.

# CODE
# ----

moneyNow = int(input('How much money do you have now: \n'))
moneyWant = int(input('How much money would you like to have: \n'))
if moneyNow == moneyWant:
    print('You have that amount of money!')
elif moneyNow > moneyWant:
    moneySpend = moneyNow - moneyWant
    print('you need to spend $' + str(moneySpend) + ' to get to the balance you want.')
elif moneyNow < moneyWant:
    moneySave = moneyWant - moneyNow
    print('you need to save $' + str(moneySave) + ' to reach your goal.')