################################################################################
#                           Functioning Clock                                  #
#                                                                              #
# PROGRAMMER:       Ben McEwen                                                 #
# CLASS:            CG120                                                      #
# ASSIGNMENT:       Assignment 7                                               #
# INSTRUCTOR:       Dean Zeller                                                #
# TA:               Robert Carver                                              #
# SUBMISSION DATE:  11/16/2015                                                 #
#                                                                              #
# DESCRIPTION:                                                                 #
#   Simple Analog Clock                                                        #
#                                                                              #
# COPYRIGHT:                                                                   #
# This program is (c) 2018 Ben McEwen and Dean Zeller. This is original        #
# work, without use of outside sources.                                        #
################################################################################
from tkinter import *
from math import cos, sin
from time import localtime


#####################################################################
# drawcircle                                                        #
#                                                                   #
# purpose:                                                          #
#      draws a circle base on center coord radius and color         #
# parameters:                                                       #
#     (Alpha,Beta,Rayon,Color,can)                                  #
# return value: none                                                #
#####################################################################
def drawcircle(Alpha, Beta, Rayon, Color, can):
    x1, y1, x2, y2 = Alpha - Rayon, Beta - Rayon, Alpha + Rayon, Beta + Rayon
    can.create_oval(x1, y1, x2, y2, fill=Color)

    #####################################################################
    # drawHourhand                                                      #
    #                                                                   #
    # purpose:                                                          #
    #     draws the hour hand                                           #
    # parameters:                                                       #
    #     (CoordA, CoordZ, Slice, Omega, can)                           #
    # return value: none                                                #
    #####################################################################


def drawHourhand(CoordA, CoordZ, Slice, Omega, can):
    Pi = 3.141592
    Omega = ((Omega - 15)) * 30
    can.create_line(CoordA + (Slice / 3) * cos(Pi * (Omega / 180)), CoordZ + (Slice / 3) * sin(Pi * (Omega / 180)),
                    CoordA - (Slice / 8) * cos(Pi * (Omega / 180)), CoordZ - (Slice / 8) * sin(Pi * (Omega / 180)),
                    fill="black", width=3)

    #####################################################################
    # drawMinhand                                                       #
    #                                                                   #
    # purpose:                                                          #
    #     draw the minute hand                                          #
    # parameters:                                                       #
    #      (CoordA, CoordZ, Slice, Omega, can)                          #
    # return value: none                                                #
    #####################################################################


def drawMinhand(CoordA, CoordZ, Slice, Omega, can):
    Pi = 3.141592
    Omega = (Omega - 15) * 6
    can.create_line(CoordA + (Slice / 1.5) * cos(Pi * (Omega / 180)), CoordZ + (Slice / 1.5) * sin(Pi * (Omega / 180)),
                    CoordA - (Slice / 6) * cos(Pi * (Omega / 180)), CoordZ - (Slice / 6) * sin(Pi * (Omega / 180)),
                    fill="blue", width=3)

    #####################################################################
    # drawSechand                                                       #
    #                                                                   #
    # purpose:                                                          #
    #     #draw the second hand                                         #
    # parameters:                                                       #
    #     none                                                          #
    # return value: none                                                #
    #####################################################################


def drawSechand(CoordA, CoordZ, Slice, Omega, can):
    Pi = 3.141592
    Omega = (Omega - 15) * 6
    can.create_line(CoordA + (Slice / 1.5) * cos(Pi * (Omega / 180)), CoordZ + (Slice / 1.5) * sin(Pi * (Omega / 180)),
                    CoordA - (Slice / 6) * cos(Pi * (Omega / 180)), CoordZ - (Slice / 6) * sin(Pi * (Omega / 180)),
                    fill="red", width=1)

    #####################################################################
    # fondclock                                                         #
    #                                                                   #
    # purpose:                                                          #
    #     draws the backgroud of the clock                              #
    # parameters:                                                       #
    #     none                                                          #
    # return value: none                                                #
    #####################################################################


def fondclock(CoordA, CoordZ, Slice, can1):
    Pi = 3.141592
    drawcircle(CoordA + 3, CoordZ + 6, Slice + (Slice / 10), "grey3", can1)  # drawing the surrounding of the clock
    drawcircle(CoordA - 1, CoordZ - 1, Slice + (Slice / 20), "cornsilk2", can1)  # drawing the surrounding of the clock
    drawcircle(CoordA, CoordZ, Slice, "azure3", can1)  # backgroud
    drawcircle(CoordA, CoordZ, Slice / 80, "black", can1)  # central point/needle articulation
    can1.create_line(CoordA + (Slice - (Slice / 30)), CoordZ, CoordA + (Slice - (Slice / 5)), CoordZ, fill="black",
                     width=3)  # 3 o'clock tick
    can1.create_line(CoordA, CoordZ + (Slice - (Slice / 30)), CoordA, CoordZ + (Slice - (Slice / 5)), fill="black",
                     width=3)  # 6 o'clock tick
    can1.create_line(CoordA - (Slice - (Slice / 30)), CoordZ, CoordA - (Slice - (Slice / 5)), CoordZ, fill="black",
                     width=3)  # 9 o'clock tick
    can1.create_line(CoordA, CoordZ - (Slice - (Slice / 30)), CoordA, CoordZ - (Slice - (Slice / 5)), fill="black",
                     width=3)  # 12 o'clock tick

    # defines the position of the ticks for 1,2,4,5,7,8,10 & 11
    can1.create_line(CoordA + (Slice / 1.05) * cos(Pi * (30 / 180)), CoordZ + (Slice / 1.05) * sin(Pi * (30 / 180)),
                     CoordA + (Slice / 1.20) * cos(Pi * (30 / 180)), CoordZ + (Slice / 1.20) * sin(Pi * (30 / 180)))
    can1.create_line(CoordA + (Slice / 1.05) * cos(Pi * (60 / 180)), CoordZ + (Slice / 1.05) * sin(Pi * (60 / 180)),
                     CoordA + (Slice / 1.20) * cos(Pi * (60 / 180)), CoordZ + (Slice / 1.20) * sin(Pi * (60 / 180)))

    can1.create_line(CoordA - (Slice / 1.05) * cos(Pi * (30 / 180)), CoordZ - (Slice / 1.05) * sin(Pi * (30 / 180)),
                     CoordA - (Slice / 1.20) * cos(Pi * (30 / 180)), CoordZ - (Slice / 1.20) * sin(Pi * (30 / 180)))
    can1.create_line(CoordA - (Slice / 1.05) * cos(Pi * (60 / 180)), CoordZ - (Slice / 1.05) * sin(Pi * (60 / 180)),
                     CoordA - (Slice / 1.20) * cos(Pi * (60 / 180)), CoordZ - (Slice / 1.20) * sin(Pi * (60 / 180)))

    can1.create_line(CoordA + (Slice / 1.05) * cos(Pi * (30 / 180)), CoordZ - (Slice / 1.05) * sin(Pi * (30 / 180)),
                     CoordA + (Slice / 1.20) * cos(Pi * (30 / 180)), CoordZ - (Slice / 1.20) * sin(Pi * (30 / 180)))
    can1.create_line(CoordA + (Slice / 1.05) * cos(Pi * (60 / 180)), CoordZ - (Slice / 1.05) * sin(Pi * (60 / 180)),
                     CoordA + (Slice / 1.20) * cos(Pi * (60 / 180)), CoordZ - (Slice / 1.20) * sin(Pi * (60 / 180)))

    can1.create_line(CoordA - (Slice / 1.05) * cos(Pi * (30 / 180)), CoordZ + (Slice / 1.05) * sin(Pi * (30 / 180)),
                     CoordA - (Slice / 1.20) * cos(Pi * (30 / 180)), CoordZ + (Slice / 1.20) * sin(Pi * (30 / 180)))
    can1.create_line(CoordA - (Slice / 1.05) * cos(Pi * (60 / 180)), CoordZ + (Slice / 1.05) * sin(Pi * (60 / 180)),
                     CoordA - (Slice / 1.20) * cos(Pi * (60 / 180)), CoordZ + (Slice / 1.20) * sin(Pi * (60 / 180)))
    #####################################################################
    # rollCredits                                                       #
    #                                                                   #
    # purpose:                                                          #
    #     roll credits                                                  #
    # parameters:                                                       #
    #     (Gamma, Pi, Epsilon)                                          #
    # return value: none                                                #
    #####################################################################


def rollCredits(event):
    can1.delete(ALL)
    creditText = """
    Tick Tock
    by
    Ben McEwen

    Completed as part of a CG120 assignment.

    Calculations based on info found at
    wikipedia.org/wiki/Clock_angle_problem#Math_problem

    CLOCK DESIGN
    Ben McEwen

    Inception of Time 
    Cronos

    (c)2018 Ben McEwen Productions, all rights reserved."""
    can2 = Canvas(root,bg="white", highlightbackground="black", highlightthickness=5, height=300, width=1000, bd= 0)
    can2.pack(fill = X)
 

    credits = can2.create_text(500, 300, text=creditText, font=("Courier", 9), justify=CENTER)
    
    for i in range(150):
        can2.move(credits, 0, -1)
        can2.after(8)
        can2.update()


# PRINCIPLE FUNCTION

#####################################################################
# Clock1                                                            #
#                                                                   #
# purpose:                                                          #
#     extracts time for math reference                              #
# parameters:                                                       #
#     (Gamma, Pi, Epsilon)                                          #
# return value: none                                                #
#####################################################################
def CLOCK1(Gamma, Pi, Epsilon):
    fondclock(Gamma, Pi, Epsilon, can1)  # extracting time value
    time = localtime()
    hour = time[3]
    minute = time[4]
    second = time[5]

    print(hour, minute, second)  # a simple test to watch what the program is doing

    drawHourhand(Gamma, Pi, Epsilon, hour, can1)
    drawMinhand(Gamma, Pi, Epsilon, minute, can1)
    drawSechand(Gamma, Pi, Epsilon, second, can1)
    root.after(1000, lambda: CLOCK1(500, 250, 200))


# execution of the main function

root = Tk()

mainLabel = Label(root, text=" Tick Tock ")
mainLabel.pack()

frame1 = Frame(root,bg="white", highlightbackground="black", highlightcolor="black", highlightthickness=5, width=90, bd= 0)
frame1.pack(fill = Y, side=LEFT)

frame2 = Frame(root,bg="white", highlightbackground="black", highlightcolor="black", highlightthickness=5, width=590, height=500, bd= 0)
frame2.pack()

can1 = Canvas(frame2,bg="white", height=500, width=1000)
can1.pack()


button_1 = Button(frame1, text="Roll Credits")
button_1.bind("<Button-1>", rollCredits)
button_1.pack()

CLOCK1(500, 250, 200)


root.mainloop()
