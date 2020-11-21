# Assignment
# -----------
# Post a Python program that accepts at least two values as input, 
# performs some computation and displays at least one value as the result. 
# The computation must involve calling one of the predefined functions in the math library. 
# Include comments in your program that describe what the program does. 
# Also post a screen shot of executing your program on at least one test case.
# -----------
# DESCRIPTION
# Pipe ID, OD calculator: This program calculates the inner area and outer circumfrence of a pipe, given the overall diameter of the outside of the pipe and the material's thickness.
# -----------
# CODE
# -----------
# Imports the Math library
import math
# User inputs the outer diameter of the pipe in cm, the value is logged as pipeOD
pipeOD = eval(input("What is the outer diameter of the pipe in cm?\n"))
# User inputs the thickness of the material in cm, the value is logged as pipeT
pipeT = eval(input("What is the materials thickness in cm?\n"))
# Calculate the inner diameter (pipeID) of the pipe and the inner radius (pipeIR) of the pipe (radius is d/2)
pipeID = pipeOD - pipeT
pipeIR = pipeID/2
# Calculate the area of the inside of the pipe using A = pi(r)^2, log as pipeIArea
pipeIArea = round(math.pi * (pipeIR * pipeIR), 2)
# Calculate the outer circumfrence of the pipe using C = pi(d), log as pipeOC
pipeOC = round(math.pi * (pipeOD), 2)

# If pipeID is less than 0, it is not a pipe, there is no inner diameter.
if pipeID > 0:
    # Print the values in a digestable format, be sure to include str() function so that the print() function can properly parse out float types.
    print("The outer circumfrence of the pipe is: \n" + str(pipeOC) + "cm.")
    print("The inner area of the pipe is: \n" + str(pipeIArea) + "cm^2.")
else:
    print("This is not a pipe.")