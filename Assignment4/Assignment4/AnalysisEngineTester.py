################################################################################
#                   Analysis Engine Tester                                     #
#                                                                              #
# PROGRAMMER:       Ben McEwen                                                 #
# CLASS:            Cg120                                                      #
# ASSIGNMENT:       Assignment 4                                               #
# INSTRUCTOR:       Dean Zeller                                                #
# TA:               Robert Carver                                              #
# SUBMISSION DATE:  10-12-2018                                                 #
#                                                                              #
# DESCRIPTION:                                                                 #
# This program is the tester for the Analysis Engine.  It creates a study      #
# and prints the report.                                                       #
#                                                                              #
# COPYRIGHT:                                                                   #
# This program is (c) 2018 Ben McEwen and Dean Zeller. This is original        #
# work, without use of outside sources.                                        #
################################################################################
from AnalysisEngine import AnalysisEngine

study1 = AnalysisEngine()
study1.introduction()
study1.gatherData()
study1.performCalculations()
study1.printReport()
study1.closing()
