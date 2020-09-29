################################################################################
#                            Occupational Projections                          #
#                                                                              #
# PROGRAMMER:       Ben McEwen                                                 #
# CLASS:            CG120                                                      #
# ASSIGNMENT:       Final Project                                              #
# INSTRUCTOR:       Dean Zeller                                                #
# TA:               Robert Carver                                              #
# SUBMISSION DATE:  December 1 2018                                            #
#                                                                              #
# DESCRIPTION:                                                                 #
# I used this opportunity to learn how to create a user interface,             #
# import data from an Excel file, and display a visual representation          #
# of data                                                                      #
#                                                                              #
# EXTERNAL FILES:                                                              #
# This program references the following files:                                 #
# occupationaldata.xlsx                                                        #
#                                                                              #
# COPYRIGHT:                                                                   #
# This program is (c) 2018 Ben McEwen. Outside learning resources are cited.   #
################################################################################
from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import *
import xlrd
import seaborn
from tkinter import ttk  # for styling

seaborn.set()

# section defines data for Graph 1
file_location = "occupationaldata.xlsx"
workbook = xlrd.open_workbook(file_location)
Table_1_3 = workbook.sheet_by_index(3)
for col in range(Table_1_3.ncols):
    xaxes = Table_1_3.col_values(0, start_rowx=4, end_rowx=14)  # (self, colx, start_rowx=, end_rowx=)
    yaxes = Table_1_3.col_values(6, start_rowx=4, end_rowx=14)

Data1 = {'Occupational Field': xaxes, 'Median Salary': yaxes}

df1 = DataFrame(Data1, columns=['Occupational Field', 'Median Salary'])
df1 = df1[['Occupational Field', 'Median Salary']].groupby('Occupational Field').sum()

# section defines data for Graph 2
for col in range(Table_1_3.ncols):
    xaxes2 = Table_1_3.col_values(0, start_rowx=4, end_rowx=14)
    yaxes2 = Table_1_3.col_values(5, start_rowx=4, end_rowx=14)

Data2 = {'Occupational Field': xaxes2, 'Percent Increase': yaxes2}

df2 = DataFrame(Data2, columns=['Occupational Field', 'Percent Increase'])
df2 = df2[['Occupational Field', 'Percent Increase']].groupby('Occupational Field').sum()

# defining Data for Graph 3
for col in range(Table_1_3.ncols):
    xaxes3 = Table_1_3.col_values(0, start_rowx=4, end_rowx=14)
    yaxes3 = Table_1_3.col_values(4, start_rowx=4, end_rowx=14)

Data3 = {'Occupational Field': xaxes3, 'Number Increase': yaxes3}

df3 = DataFrame(Data3, columns=['Occupational Field', 'Number Increase'])
df3 = df3[['Occupational Field', 'Number Increase']].groupby('Occupational Field').sum()


# draws Graph1
def drawgraph1(event):
    figure1 = plt.figure(figsize=(6, 6), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, frame2)
    plt.subplots_adjust(bottom=.45, left=.2)
    bar1.get_tk_widget().pack(side=tk.LEFT)
    df1.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_xlabel('Occupational Fields')
    ax1.set_ylabel('Salary In Dollars')
    ax1.set_title('Median Annual Wage(2017) by Occupational Field')


# draws Graph2
def drawgraph2(event):
    figure2 = plt.figure(figsize=(6, 6), dpi=100)
    ax2 = figure2.add_subplot(111)
    bar2 = FigureCanvasTkAgg(figure2, frame2)
    plt.subplots_adjust(bottom=.45)
    bar2.get_tk_widget().pack(side=tk.LEFT)
    df2.plot(kind='bar', legend=True, ax=ax2)
    ax2.set_xlabel('Occupational Fields')
    ax2.set_ylabel('Increase in Number of Jobs \n (percent)')
    ax2.set_title('Percent increase in number of jobs(16-26)')


# draws Graph3
def drawgraph3(event):
    figure3 = plt.figure(figsize=(6, 6), dpi=100)
    ax3 = figure3.add_subplot(111)
    bar3 = FigureCanvasTkAgg(figure3, frame2)
    plt.subplots_adjust(bottom=.45)
    bar3.get_tk_widget().pack(side=tk.LEFT)
    df3.plot(kind='bar', legend=True, ax=ax3)
    ax3.set_xlabel('Occupational Fields')
    ax3.set_ylabel('Increase in number of Jobs(#) \n (thousands)')
    ax3.set_title('Number increase in number of jobs(16-26)')


def showsources(event):
    # canvas_graph.delete(ALL)
    sources_text = """
    Occupation Projections
    by
    Ben McEwen

    Completed as GC120 Final Project.

    Data based on info found at:
    Bureau of Labor Statistics
    https://www.bls.gov/emp/data/occupational-data.htm

    Learning resources for creating code:
        Video Tutorial Series:
            Python Gui: https://www.youtube.com/watch?v=RJB1Ek2Ko_Y&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d   Matplotlib: https://www.youtube.com/watch?v=q7Bo_J8x_dw
            
        Websites:
            http://pandas.pydata.org/pandas-docs/stable/   https://matplotlib.org/3.0.2/index.html   https://docs.python.org/3/library/tkinter.html
            
    GUI DESIGN
    Ben McEwen

    (c)2018 Ben McEwen Productions, all rights reserved."""
    can2 = Canvas(root, bg="white", highlightbackground="black", highlightthickness=5, height=500, bd=0)
    can2.pack(fill=X)

    sources: object = can2.create_text(900, 300, text=sources_text, font=("Courier", 9), justify=CENTER)

    for i in range(600):
        can2.move(sources, 0, -1)
        can2.after(8)
        can2.update()


def donothing():
    print("ok ok i wont")


root = tk.Tk()

#  Changes Main Window Icon
tk.Tk.iconbitmap(root, 'clienticon.ico')

#  Changes Main Window Label
tk.Tk.wm_title(root, "Occupational Projections")

# creates drop down menus
menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="file", menu=subMenu)
subMenu.add_command(label="New Project...", command=donothing)
subMenu.add_command(label="New ", command=donothing)
subMenu.add_command(label="New ", command=donothing)

subMenu.add_separator()
subMenu.add_command(label="Exit", command=donothing)

editMenu = Menu(menu)
menu.add_cascade(label="edit", menu=editMenu)
editMenu.add_command(label="Redo", command=donothing)
editMenu.add_command(label="New ", command=donothing)
editMenu.add_command(label="New ", command=donothing)

# creates main label
mainLabel = Label(root, text=" Occupational Projections ")
mainLabel.pack()

# defines frames
frame1 = Frame(root, bg="white", highlightbackground="black", highlightcolor="black", highlightthickness=5, bd=0)
frame1.pack(fill=X, side=TOP)

frame2 = Frame(root, bg="white", highlightbackground="black", highlightcolor="black", highlightthickness=5,
               bd=0)
frame2.pack(fill=BOTH)

# defines tool bars

toolbar = Frame(root, bg="blue")

button_1 = ttk.Button(frame1, text="Median Salary")
button_1.bind("<Button-1>", drawgraph1)
button_1.pack(side=LEFT)

button_2 = ttk.Button(frame1, text="% increase")
button_2.bind("<Button-1>", drawgraph2)
button_2.pack(side=LEFT)

button_3 = ttk.Button(frame1, text="# increase")
button_3.bind("<Button-1>", drawgraph3)
button_3.pack(side=LEFT)

button_4 = ttk.Button(frame1, text="Sources")
button_4.bind("<Button-1>", showsources)
button_4.pack(side=LEFT)

toolbar.pack(side=TOP, fill=X)

# Defines Status bar
status = Label(root, text="Preparing to do nothing", bd=1, relief=SUNKEN, anchor=W, )
status.pack(side=BOTTOM, fill=X, )

root.mainloop()
