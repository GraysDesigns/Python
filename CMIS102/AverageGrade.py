# Assignment
# ----------
# write a Python program to compute the average quiz grade for a group of five students. 
# Your program should include a list of five names. 
# Using a for loop, it should successively prompt the user for the quiz grade for each of the five students. 
# Each prompt should include the name of the student whose quiz grade is to be input. 
# It should compute and display the average of those five grades and the highest grade. 
# You should decide on the names of the five students.
# ---------
# CODE 
# ---------

# Define a list with all the names of the students.
students = ['Tim', 'Kate', 'Igor', 'Beth', 'Jonny']
# Define an empty list that will be populated with the grades
grades = []
# populate the list by asking what each students grade was
for i in students:
    grades.append(eval(input("What was " + i + "'s Grade: ")))

# use a simple sum for loop to calculate the total sum of all grades
total = 0
for i in grades:
    total += i

# to get the average of the grades, the total is divided by len(students) (or 5)
avg = total/len(students)

# print the average
print("The average score was:", avg)

