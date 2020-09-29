################################################################################
#                           Objects                                            #
#                                                                              #
# PROGRAMMER:       Ben McEwen                                                 #
# CLASS:            CG120                                                      #
# ASSIGNMENT:       Assignment 2                                               #
# INSTRUCTOR:       Dean Zeller                                                #
# TA:               Robert Carver                                              #
# SUBMISSION DATE:  9/7/2018                                                   #
#                                                                              #
# DESCRIPTION:                                                                 #
# This program will calculate the sum and average of 3 user defined integers   #  
# for three separate studies.                                                  #
#                                                                              #
# COPYRIGHT:                                                                   #
# This program is (c) 2018 Ben McEwen and Dean Zeller. This is original work,  #
# without use of outside sources.                                              #
################################################################################
import time
class AnalysisEngine:

#####################################################################
# method-name: greeting                                             #
#                                                                   #
# parameters: none                                                  #
# return value: none                                                #
#####################################################################

    def greeting (self):
        print("Initializing Attributes")
        print()
        print("Welcome to Assignment 2, Objects")
        time.sleep(.5)
        print()
    
#####################################################################
# method-name: _init_                                               #
#                                                                   #
# parameters: none                                                  #
# return value: none                                                #
#####################################################################

    def __init__ (self):
        self.data1 = 0
        self.data2 = 0
        self.data3 = 0
        self.sum = 0
        self.average = 0
        
#####################################################################
# method-name: enterData                                            #
#                                                                   #
# parameters: none                                                  #
# return value: none                                                #
#####################################################################

    def enterData (self):
        userName = input("Please provide your name => ")
        print()
        print("Greating, wise and powerfull "+ userName +"!")
        time.sleep(.5)
        print()
        print("Introdution:")
        print("This program will calculate basic statistics on three integer numbers,")
        print("for three separate studies. It will run in three phases per study:")
        time.sleep(1)
        print("    Phase 1 - Gather Input from User")
        time.sleep(.5)
        print("    Phase 2 - Calculate Sum and Average")
        time.sleep(.5)
        print("    Phase 3 - Output Results")
        time.sleep(.5)
        print()
        print("--------------------------------")
        print("Phase 1 - Gather Input from User")
        print("--------------------------------")
        time.sleep(.5)
        self.data1 = int(input("    Enter data => "))
        self.data2 = int(input("    Enter data => "))
        self.data3 = int(input("    Enter data => "))
        self.calculatesum = (self.data1 + self.data2 + self.data3)
        self.calculateaverage = ((self.data1 + self.data2 + self.data3)/3)

#####################################################################
# method-name: phaseTrans1_2                                        #
#                                                                   #
# parameters: none                                                  #
# return value: none                                                #
#####################################################################

    def phaseTrans1_2 (self):
        print()
        print("Phase 1 complete")
        print("Continuing to phase 2")
        time.sleep(.5)
        print()
        print("-----------------------------------")
        print("Phase 2 - Calculate Sum and Average")
        print("-----------------------------------")
        time.sleep(.5)
            
#####################################################################
# method-name: phaseTrans2_3                                        #
#                                                                   #
# parameters: none                                                  #
# return value: none                                                #
#####################################################################

    def phaseTrans2_3 (self):
        print()
        print("Phase 2 complete")
        print("Continuing to phase 3")
        time.sleep(.5)
        print()
        print("------------------------")
        print("Phase 3 - Output Results")
        print("------------------------")
        time.sleep(.5)

#####################################################################
# method-name: printData                                            #
#                                                                   #
# parameters: none                                                  #
# return value: none                                                #
#####################################################################

    def printData (self):
        print("You have entered: ", self.data1, self.data2, self.data3)
        time.sleep(.5)
        
#####################################################################
# method-name:calcSum                                               #
#                                                                   #
# parameters: none                                                  #
# return value: none                                                #
#####################################################################

    def calcSum (self):
        print()
        self.sum = self.calculatesum
        print("The sum has been calculated.")
        time.sleep(.5)
        
#####################################################################
# method-name: calcAverage                                          #
#                                                                   #
# parameters: none                                                  #
# return value: none                                                #
#####################################################################

    def calcAverage (self):
        self.average = self.calculateaverage
        print("The average has been calculated.")


#####################################################################
# method-name:printReport                                           #
#                                                                   #
# parameters: none                                                  #
# return value: none                                                #
#####################################################################

    def printReport (self):
        print()
        print("The sum of your data is:", self.sum)
        print("The average of your data is:", self.average)
        time.sleep(.5)
    
#####################################################################
# method-name: goodbye                                              #
#                                                                   #
# parameters: none                                                  #
# return value: none                                                #
#####################################################################

    def goodbye (self):
        print()
        print("Summary Complete")
        input("\nPress the enter key to exit.")

#####################################################################
# method-name: lblsummary                                           #
#                                                                   #
# parameters: none                                                  #
# return value: none                                                #
#####################################################################

    def lblsummary (self):
        print("------------------")
        print("Summary of reports")
        print("------------------")
        time.sleep(.5)
        
#####################################################################
# method-name: lblstudy1                                            #
#                                                                   #
# parameters: none                                                  #
# return value: none                                                #
#####################################################################

    def lblstudy1 (self):
        print("-------")
        print("Study 1")
        print("-------")
        time.sleep(.5)
        
#####################################################################
# method-name: lblstudy2                                            #
#                                                                   #
# parameters: none                                                  #
# return value: none                                                #
#####################################################################

    def lblstudy2 (self):
        print("-------")
        print("Study 2")
        print("-------")
        time.sleep(.5)

#####################################################################
# method-name: lblstudy3                                            #
#                                                                   #
# parameters: none                                                  #
# return value: none                                                #
#####################################################################

    def lblstudy3 (self):
        print("-------")
        print("Study 3")
        print("-------")
        time.sleep(.5)
