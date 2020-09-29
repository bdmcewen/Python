################################################################################
#                           Basic Calculations                                 #
#                                                                              #
# PROGRAMMER:       Ben McEwen                                                 #
# CLASS:            CG120                                                      #
# ASSIGNMENT:       Assignment 1                                               #
# INSTRUCTOR:       Dean Zeller                                                #
# TA:               Robert Carver                                              #
# SUBMISSION DATE:  8/31/2018                                                  #
#                                                                              #
# DESCRIPTION:                                                                 #
# This program will calculate the sum and average of 3 user defined integers.  #
#                                                                              #
# COPYRIGHT:                                                                   #
# This program is (c) 2018 Ben McEwen and Dean Zeller. This is original work,  #
# without use of outside sources.                                              #
################################################################################
import time
print()
print("Welcome to Assignment 1, Basic Calculations")
time.sleep(.5)
print()

userName = input("Please provide your name => ")
print("Hello,",userName)
time.sleep(.5)
print ()

print("Introdution:")
print("This program will calculate basic statistics on three integer numbers.")
print("It will run in three phases:")
time.sleep(1)
print("    Phase 1 - Gather Input from User")
time.sleep(.5)
print("    Phase 2 - Calculate Sum and Average")
time.sleep(.5)
print("    Phase 3 - Output Results")
time.sleep(.5)
print()

#################################################################################
# Phase 1 -- Gather input from user                                             #
#################################################################################

print("--------------------------------------------------------------------------------")
print("Phase 1 - Gather Input from User")
print("--------------------------------------------------------------------------------")
print()
time.sleep(.5)

print("Please enter three numbers. Only enter integer values, as error-checking")
print("has not yet been implemented. Let's begin!")
time.sleep(1)
print()

firstNumber = int(input("    Please enter a number          =>"))
secondNumber = int(input("    Now, enter a second number     =>"))
thirdNumber = int(input("    Finally, enter a third number  =>"))
print()

print("Thank you",userName,",you have entered: "+str(firstNumber)+","+str(secondNumber)+" and "+str(thirdNumber))
time.sleep(.5)

print()
print("Phase 1 Complete")
print()
time.sleep(.5)
print("Congratulations! You did great!")
print()
time.sleep(.5)
print("Continuing to Phase 2.")
time.sleep(1)      
print()

#################################################################################
# Phase 2 -- Calculate Sum and Average                                          #
#################################################################################

print("--------------------------------------------------------------------------------")
print("Phase 2 - Calculate Sum and Average")
print("--------------------------------------------------------------------------------")
time.sleep(.5)
print("    Calculated sum")
time.sleep(.5)
print("    Calculated average")
print()
time.sleep(.5)
print("Phase 2 Complete")
time.sleep(1)
print()

################################################################################
# Phase 3 - Output Results                                                     #
################################################################################
print("--------------------------------------------------------------------------------")
print("Phase 3 - Output Results")
print("--------------------------------------------------------------------------------")
time.sleep(.5)
print("Data:    "+str(firstNumber)+","+str(secondNumber)+" and "+str(thirdNumber))
time.sleep(.5)

Sum=(firstNumber+secondNumber+thirdNumber)
print("Sum:    ",Sum)
time.sleep(.5)
Average=((firstNumber+secondNumber+thirdNumber)/3)
print("Average:",Average)
time.sleep(.5)
print()

print("Phase 3 Complete")
time.sleep(1)
print()

print("Exiting program")
