################################################################################
#                           More Processing                                    #
#                                                                              #
# PROGRAMMER:       Ben McEwen                                                 #
# CLASS:            CG120                                                      #
# ASSIGNMENT:       Assignment 5                                               #
# INSTRUCTOR:       Dean Zeller                                                #
# TA:               Robert Carver                                              #
# SUBMISSION DATE:  10/19/2018                                                 #
#                                                                              #
# DESCRIPTION:                                                                 #
# This is an Analysis Engine.  It's purpose is to find various                 #
# statistical computations such as mean median mode variance and               #   
# standard deviation.                                                          #
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
        self.leader         = ""
        self.title          = ""
        self.data           = []
        self.sum            = 0.0
        self.average        = 0.0
        self.variance       = 0.0
        self.stdev          = 0.0
        self.nsize          = 0.0
        self.harmonicMean   = 0.0
        self.min            = 0.0
        self.max            = 0.0
        self.median         = 0.0
        self.pvariance      = 0.0
        self.pstdev         = 0.0

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
        while(True):
            try:
                response = input("    Size of Dataset => ") 
                self.nsize = int(response)                  
                break                                       
            except ValueError:
                print(response,"is not an integer value.")
                print("Please enter an integer value.")
        print()
        print("You entered",self.nsize)
        print()

        print("Data will have",self.nsize,"elements, indexed from 0 to",str(self.nsize - 1)+".")
        print()
        print("Enter integer and floating-point values:")
        
        for n in range(self.nsize):
            while(True):
                try:
                    response = input("    Enter data point => ")
                    index = float(response)
                    self.data.append(index)
                    break
                except ValueError:
                    print(response,"is not a floating-point value.")
                    print("Please enter a floating-point value.")
        self.data.sort()        
        print("Data entered: ")
        print("    ", end="")
        for i in range(len(self.data)):        
            if i < len(self.data)-1:
                print(self.data[i], end=", ")  
            else:
                print(self.data[i])            


        print()
        print("Phase 1 complete.")
        print()
        input("\n(Pausing -- press enter to continue)")

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
    # calcharmonicMean                                                  #
    #                                                                   #
    # purpose:                                                          #
    #     - calculate and print the (sample) standard deviation of      #
    #       self.data                                                   #
    # parameters: none                                                  #
    # return value: none                                                #
    #####################################################################
    def calcharmonicMean(self):
        n = len(self.data)
        denom = 0.0
        for i in self.data:
            denom += (1/i)
                    
        self.harmonicMean = n/denom
        print("    Calculated harmonic mean ("+str(self.harmonicMean)+")")

    #####################################################################
    # calcmin                                                           #
    #                                                                   #
    # purpose:                                                          #
    #     - calculate and print the (sample) standard deviation of      #
    #       self.data                                                   #
    # parameters: none                                                  #
    # return value: none                                                #
    #####################################################################
    def calcmin(self):
        self.min = self.data[0]
        print("    Determined minimum datum ("+str(self.min)+")")

    #####################################################################
    # calcmax                                                           #
    #                                                                   #
    # purpose:                                                          #
    #     - calculate and print the (sample) standard deviation of      #
    #       self.data                                                   #
    # parameters: none                                                  #
    # return value: none                                                #
    #####################################################################
    def calcmax(self):
        self.data.reverse()
        self.max = self.data[0]
        print("    Determined maximum datum ("+str(self.max)+")")
        self.data.reverse()

    #####################################################################
    # calcmedian                                                        #
    #                                                                   #
    # purpose:                                                          #
    #     - calculate and print the (sample) standard deviation of      #
    #       self.data                                                   #
    # parameters: none                                                  #
    # return value: none                                                #
    #####################################################################
    def calcmedian(self):
        n = len(self.data)
        if (n % 2 ==0):
            self.median = (self.data[n//2] + self.data[n//2-1]/2)
        else:
            self.median = self.data[(n-1)//2]
        print("    Calculated median ("+str(self.median)+")")

    #####################################################################
    # calcpvariance                                                     #
    #                                                                   #
    # purpose:                                                          #
    #     - calculate and print the variance of self.data               #
    # parameters: none                                                  #
    # return value: none                                                #
    #####################################################################
    def calcpvariance(self):
        n = len(self.data)
        self.pvariance = sum((self.average - x) ** 2 for x in self.data) / float(n)
        print("    Calculated Pop. variance ("+str(self.pvariance)+")")

    #####################################################################
    # calcPstDev                                                        #
    #                                                                   #
    # purpose:                                                          #
    #     - calculate and print the (sample) standard deviation of      #
    #       self.data                                                   #
    # parameters: none                                                  #
    # return value: none                                                #
    #####################################################################
    def calcpstdev(self):
        self.pstdev = math.sqrt(self.pvariance)
        print("    Calculated Pop. standard deviation ("+str(self.pstdev)+")")
        
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
        self.calcharmonicMean()   
        self.calcmin()            
        self.calcmax()      
        self.calcmedian()         
        self.calcpvariance()     
        self.calcpstdev()        
        print("Phase 2 complete")
        print()
        input("\n(Pausing -- press enter to continue)")
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
        
        actualsum       = sum(self.data)
        actualmean       = statistics.mean(self.data)
        actualvariance   = statistics.variance(self.data)
        actualstdev      = statistics.stdev(self.data)
        actualhmean      = statistics.harmonic_mean(self.data)
        actualmin        = min(self.data)
        actualmax        = max(self.data)
        actualmedian     = statistics.median(self.data)
        actualpvariance  = statistics.pvariance(self.data)
        actualpstdev     = statistics.pstdev(self.data) 
        
        print("Phase 3:  Output table")
        print("----------------------")
        print()
        horizLine = "+----------------------------------------------------+"   
        
        print(horizLine)
        print("| %-50s |" %(self.title))
        print("| %-50s |" %(self.leader))
       
        print(horizLine)
        print("|                            "," %10s " % ("Calculated"),                          " %8s |" % ("Actual"))
        print("| Sum:                       "," %10s " % ("{:.3f}".format(self.sum)),             " %8s |" % ("{:.3f}".format(actualsum)))
        print("| Mean:                      "," %10s " % ("{:.3f}".format(self.average)),         " %8s |" % ("{:.3f}".format(actualmean)))
        print("| Sample Variance:           "," %10s " % ("{:.3f}".format(self.variance)),        " %8s |" % ("{:.3f}".format(actualvariance)))
        print("| Sample Standard Deviation: "," %10s " % ("{:.3f}".format(self.stdev)),           " %8s |" % ("{:.3f}".format(actualstdev)))
        print("| Harmonic Mean:             "," %10s " % ("{:.3f}".format(self.harmonicMean)),    " %8s |" % ("{:.3f}".format(actualhmean)))
        print("| Minimum:                   "," %10s " % ("{:.3f}".format(self.min)),             " %8s |" % ("{:.3f}".format(actualmin)))
        print("| Maximum:                   "," %10s " % ("{:.3f}".format(self.max)),             " %8s |" % ("{:.3f}".format(actualmax)))
        print("| Median:                    "," %10s " % ("{:.3f}".format(self.median)),          " %8s |" % ("{:.3f}".format(actualmedian)))
        print("| Pop. Var:                  "," %10s " % ("{:.3f}".format(self.pvariance)),       " %8s |" % ("{:.3f}".format(actualpvariance)))
        print("| Pop. Standard Deviation:   "," %10s " % ("{:.3f}".format(self.pstdev)),          " %8s |" % ("{:.3f}".format(actualpstdev)))
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
