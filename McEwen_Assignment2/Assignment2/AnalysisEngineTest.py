################################################################################
#                           Objects                                            #
#                                                                              #
# PROGRAMMER:       Ben McEwen                                                 #
# CLASS:            CG120                                                      #
# ASSIGNMENT:       Assignment 2                                               #
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
from AnalysisEngine import AnalysisEngine
import time



study1 = AnalysisEngine()

study1.greeting()
study1.lblstudy1()
study1.enterData()              
study1.printData()
study1.phaseTrans1_2()
study1.calcSum()               
study1.calcAverage()
study1.phaseTrans2_3()
study1.printReport()

study2 = AnalysisEngine()
study2.lblstudy2()
study2.enterData()              
study2.printData()
study2.phaseTrans1_2()
study2.calcSum()               
study2.calcAverage()
study2.phaseTrans2_3()
study2.printReport()

study3 = AnalysisEngine()
study3.lblstudy3()
study3.enterData()              
study3.printData()
study3.phaseTrans1_2()
study3.calcSum()               
study3.calcAverage()
study3.phaseTrans2_3()
study3.printReport()

study1.lblsummary()

study1.lblstudy1()
study1.printData()
study1.printReport()

study2.lblstudy2()
study2.printData()
study2.printReport()

study3.lblstudy3()
study3.printData()
study3.printReport()
study3.goodbye()





