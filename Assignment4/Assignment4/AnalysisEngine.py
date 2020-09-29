################################################################################
#                           Standard Deviation                                 #
#                                                                              #
# PROGRAMMER:       Ben McEwen                                                 #
# CLASS:            CG120                                                      #
# ASSIGNMENT:       Assignment 4                                               #
# INSTRUCTOR:       Dean Zeller                                                #
# TA:               Robert Carver                                              #
# SUBMISSION DATE:  10-12-2018                                                 #
#                                                                              #
# DESCRIPTION:                                                                 #
# This is the object definition template for the Analysis Engine.  It is       #
# organized to allow for additional attributes and methods to be added by      #
# students.                                                                    #
#                                                                              #
# COPYRIGHT:                                                                   #
# This program is (c) 2018 Ben McEwen and Dean Zeller. This is original        #
# work, without use of outside sources.                                        #
################################################################################
import statistics
import math

class AnalysisEngine:

    #####################################################################
    # __init__                                                          #
    #                                                                   #
    # purpose:                                                          #
    #     - initialize the attributes to default values                 #
    # parameters: none                                                  #
    # return value: none                                                #
    #####################################################################
    def __init__ (self):
        self.leader   = ""
        self.title    = ""
        self.data     = []
        self.sum      = 0.0
        self.average  = 0.0
        self.variance = 0.0
        self.stdev    = 0.0
        self.nsize    = 0.0

    #####################################################################
    # introduction                                                      #
    #                                                                   #
    # purpose:                                                          #
    #     - accept user input for user and study name                   #
    #     - display instructions for user                               #
    # parameters: none                                                  #
    # return value: none                                                #
    #####################################################################
    def introduction(self):
        print("Welcome to Assignment 4, Standard Deviation")
        print()
        self.title = input("Enter the title of the study => ")
        print("Study title set to",self.title)
        print()
        self.leader = input("Enter the head of research for this study => ")
        print("Hello,",self.leader+".")
        print("Introduction:")
        print("This program will calculate the standard deviation on")
        print("a list of values entered by the user.  It will run in")
        print("three phases:")
        print("    Phase 1 -- Gather input from user")
        print("    Phase 2 -- Calculate sum, average, variance, and stdev")
        print("    Phase 3 -- Output results")
        print()
        
    #####################################################################
    # gatherData                                                        #
    #                                                                   #
    # purpose:                                                          #
    #     - accept user input for the self.data attribute               #
    # parameters: none                                                  #
    # return value: none                                                #
    #####################################################################
    def gatherData(self):
        print("Phase 1:  Gather user input")
        print("---------------------------")
        print("To enter the data correctly, the program needs to know how many")
        print("numbers are in the dataset.")
        self.nsize = int(input("    Size of Dataset => "))
        print("Data will have",self.nsize,"elements, indexed from 0 to",str(self.nsize - 1)+".")
        print()
        print("Enter integer and floating-point values:")
        
        for n in range(self.nsize):
            index = float(input("    Enter data point => "))
            self.data.append(index)
        print("Data entered: ")
        print("    ", end="")
        for d in self.data:
            print(d, end=", ")
        print()
        print("Phase 1 complete.")
        print()

    #####################################################################
    # calcSum                                                           #
    #                                                                   #
    # purpose:                                                          #
    #     - calculate and print the sum of self.data                    #
    # parameters: none                                                  #
    # return value: none                                                #
    #####################################################################
    def calcSum(self):
        self.sum = sum(self.data)
        print("    Calculated sum ("+str(self.sum)+")")

    #####################################################################
    # calcAverage                                                       #
    #                                                                   #
    # purpose:                                                          #
    #     - calculate and print the average of self.data                #
    # parameters: none                                                  #
    # return value: none                                                #
    #####################################################################
    def calcAverage(self):
        self.average = (self.sum / self.nsize)
        print("    Calculated average ("+str(self.average)+")")

    #####################################################################
    # calcVariance                                                      #
    #                                                                   #
    # purpose:                                                          #
    #     - calculate and print the variance of self.data               #
    # parameters: none                                                  #
    # return value: none                                                #
    #####################################################################
    def calcVariance(self):
        n = len(self.data)
        self.variance = sum((self.average - x) ** 2 for x in self.data) / float(n - 1)

        print("    Calculated variance ("+str(self.variance)+")")

    #####################################################################
    # calcStdev                                                         #
    #                                                                   #
    # purpose:                                                          #
    #     - calculate and print the (sample) standard deviation of      #
    #       self.data                                                   #
    # parameters: none                                                  #
    # return value: none                                                #
    #####################################################################
    def calcStdev(self):
        self.stdev = math.sqrt(self.variance)
        print("    Calculated standard deviation ("+str(self.stdev)+")")

    #####################################################################
    # performCalculations                                               #
    #                                                                   #
    # purpose:                                                          #
    #     - perform all calculations, with appropriate header           #
    # parameters: none                                                  #
    # return value: none                                                #
    #####################################################################
    def performCalculations(self):
        print("Phase 2:  Perform Calculations")
        print("------------------------------")
        self.calcSum()
        self.calcAverage()
        self.calcVariance()
        self.calcStdev()
        print("Phase 2 complete")
        print()

    #####################################################################
    # printReport                                                       #
    #                                                                   #
    # purpose:                                                          #
    #     - print a summary report of the study                         #
    # parameters: none                                                  #
    # return value: none                                                #
    #####################################################################
    def printReport(self):
        
        actualmean = statistics.mean(self.data)
        actualvariance = statistics.variance(self.data)
        actualstdev = statistics.stdev(self.data)
        
        print("Phase 3:  Output table")
        print("----------------------")
        print()
        horizLine = "+---------------------------------------------+"   
        
        print(horizLine)
        print("| %-43s |" %(self.title))
        print("| %-43s |" %(self.leader))
       
        print(horizLine)
        print("|                     "," %10s " % ("Calculated"),                   " %8s |" % ("Actual"))
        print("| Sum:                "," %10s " % ("{:.3f}".format(self.sum)),      " %8s |" % ("{:.3f}".format(self.sum)))
        print("| Mean:               "," %10s " % ("{:.3f}".format(self.average)),  " %8s |" % ("{:.3f}".format(actualmean)))
        print("| Variance:           "," %10s " % ("{:.3f}".format(self.variance)), " %8s |" % ("{:.3f}".format(actualvariance)))
        print("| Standard Deviation: "," %10s " % ("{:.3f}".format(self.stdev)),    " %8s |" % ("{:.3f}".format(actualstdev)))
        print(horizLine)
        

    # compareResultsReport method and documentation, from step 10

    #####################################################################
    # closing                                                           #
    #                                                                   #
    # purpose:                                                          #
    #     - print closing remarks                                       #
    # parameters: none                                                  #
    # return value: none                                                #
    #####################################################################
    def closing(self):
        print("Exiting",self.title)
        print("Goodbye!")
