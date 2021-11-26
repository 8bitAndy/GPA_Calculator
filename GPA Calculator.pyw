"""
Grade Point Average Calculator by Liam Andrews
Version: 0.4
26/11/2021

 - Next version: 0.45

Need to change this new version to be more like the draft version, where it asks how many of each grade you have

TODO:
- Add settings tab
- Add ability to save results
- Change way program calculates GPA, change interface on main tab
- Add tab for WAM
- Add clear button for GPA tab


WORKING ON CURRENTLY
    - changing the way GPA is calculated
    - change gpa tab layout
"""

import tkinter
from tkinter import ttk


# Class for calculator
class GPA_Calculator:

    # Constructor method
    def __init__(self):
        # Create the main window
        self.main = tkinter.Tk()
        # Set main window title
        self.main.title('GPA Calculator')
        # Set window size
        self.main.geometry('600x400')
        # Change the window's icon
        self.main.iconbitmap('icon.ico')
        # Prevent window resizing
        self.main.resizable(0, 0)

        # Creating the tabs for the GUI, essentially two frames, either hidden or shown by using the tabs at the top of GUI
        tabControl = ttk.Notebook(self.main)
        gpaTab = tkinter.Frame(tabControl)
        wamTab = tkinter.Frame(tabControl)
        statsTab = tkinter.Frame(tabControl)
        fileTab = tkinter.Frame(tabControl)

        # Labeling the tabs appropriately
        tabControl.add(gpaTab, text='GPA Calculator')
        tabControl.add(wamTab, text='WAM Calculator')
        tabControl.add(statsTab, text='View Statistics')
        tabControl.add(fileTab, text='Save files')

        # Packing the tabs and expanding it to the entire window
        tabControl.pack(expand=True, fill="both")

        """
        GPA Calculator tab
        """

        # Strings that grades will be entered into via entry boxes in the GUI
        self.entry1String = tkinter.StringVar()
        self.entry2String = tkinter.StringVar()
        self.entry3String = tkinter.StringVar()
        self.entry4String = tkinter.StringVar()
        self.entry5String = tkinter.StringVar()

        # Instructions for the user, displayed as a label with appropriate padding
        instructionLabel = tkinter.Label(gpaTab, text='Enter the total units for each grade: ')
        instructionLabel.pack(pady=10)

        # Result 1 label
        resultLabel1 = tkinter.Label(gpaTab, text='High Distinction: ')
        resultLabel1.pack()
        # Empty text box for entering data, justify right is used to make text appear centred
        resultEntry1 = tkinter.Entry(gpaTab, textvariable=self.entry1String, justify='center')
        resultEntry1.pack()

        # Result 2 label
        resultLabel2 = tkinter.Label(gpaTab, text='Distinction: ')
        resultLabel2.pack()
        # Empty text box for entering data, justify right is used to make text appear centred
        resultEntry2 = tkinter.Entry(gpaTab, textvariable=self.entry2String, justify='center')
        resultEntry2.pack()

        # Result 3 label
        resultLabel3 = tkinter.Label(gpaTab, text='Credit: ')
        resultLabel3.pack()
        # Empty text box for entering data, justify right is used to make text appear centred
        resultEntry3 = tkinter.Entry(gpaTab, textvariable=self.entry3String, justify='center')
        resultEntry3.pack()

        # Result 4 label
        resultLabel4 = tkinter.Label(gpaTab, text='Pass: ')
        resultLabel4.pack()
        # Empty text box for entering data, justify right is used to make text appear centred
        resultEntry4 = tkinter.Entry(gpaTab, textvariable=self.entry4String, justify='center')
        resultEntry4.pack()

        # Result 5 label
        resultLabel5 = tkinter.Label(gpaTab, text='Fail: ')
        resultLabel5.pack()
        # Empty text box for entering data, justify right is used to make text appear centred
        resultEntry5 = tkinter.Entry(gpaTab, textvariable=self.entry5String, justify='center')
        resultEntry5.pack()

        # Button to calculate the GPA
        calculateButton = tkinter.Button(gpaTab, text='Calculate results', command=self.calculateGPA)
        calculateButton.pack(pady=10)

        # Contains the frame with the GPA result
        resultsFrame = tkinter.Frame(gpaTab)
        resultsFrame.pack()

        # Display for GPA within the results frame
        gpaFrame = tkinter.Frame(resultsFrame)
        gpaFrame.pack(side='left')
        gpaLabel = tkinter.Label(gpaFrame, text='Your GPA is: ')
        gpaLabel.pack(side='left')
        self.gpaResult = tkinter.Label(gpaFrame, text='0')
        self.gpaResult.pack(side='right')

        # Display the WAM within the results frame
        wamFrame = tkinter.Frame(resultsFrame)
        wamFrame.pack(side='right')
        gpaLabel = tkinter.Label(wamFrame, text='Your WAM is: ')
        gpaLabel.pack(side='left')
        self.wamResult = tkinter.Label(wamFrame, text='0')
        self.wamResult.pack(side='right')

        # Stats tab gpa label
        self.statsGPA = tkinter.Label(statsTab, text='0')
        self.statsGPA.pack()
        # stats tab wam label
        self.statsWAM = tkinter.Label(statsTab, text='0')
        self.statsWAM.pack()

        """
        File handling tab
        """

        # Button to save information to a file
        saveButton = tkinter.Button(fileTab, text='Save file', command=self.saveFile)
        saveButton.pack(pady=20)

        # Label to display notification if file has saved or not
        self.saveLabel = tkinter.Label(fileTab, text='')
        self.saveLabel.pack()

        # Enter main loop of program
        self.main.mainloop()

    # Calculates and displays GPA via the GUI, once button is pressed
    def calculateGPA(self):

        # Extract the input from all 5 entry boxes, converts all values to ints
        hd_grades = int(self.entry1String.get())
        d_grades = int(self.entry2String.get())
        cr_grades = int(self.entry3String.get())
        p_grades = int(self.entry4String.get())
        fail_grades = int(self.entry5String.get())

        # Calculate the total number units taken. Used in calculation for GPA
        unitTotal = hd_grades + d_grades + cr_grades + p_grades + fail_grades



        # Create default value to print if no score recorded, create empty list for the grades to be entered into
        gpaScore = 0.0
        # Weighted average mean
        wamScore = 0.0
        grades = []

        # Append the 4 grades into a list
        grades.append(float(self.entry1String.get()))
        grades.append(float(self.entry2String.get()))
        grades.append(float(self.entry3String.get()))
        grades.append(float(self.entry4String.get()))

        # Loop through each grade and get appropriate score
        for grade in grades:

            # Check grade and award appropriate points for them, HD = 4, D = 3.5, CR = 3, P = 2
            # High Distinction
            if grade >= 80:
                point = 4
            # Distinction
            elif grade >= 70:
                point = 3.5
            # Credit
            elif grade >= 60:
                point = 3
            # Pass
            elif grade >= 50:
                point = 2
            # Fail
            else:
                point = 0

            gpaScore += point * 15
            wamScore += grade * 15

        # Calculation for GPA
        gpaScore = gpaScore / (15 * 4)

        # Calculation for WAM
        wamScore = wamScore / (15 * 4)

        gpaScore = 0
        # Multiply amount of each grade by 15 points to get GPA, then divide by total amount of units
        gpaScore = (((hd_grades * 4) * 15) + ((d_grades * 3.5) * 15) + ((cr_grades * 3) * 15) + ((p_grades * 2) * 15) + ((fail_grades * 0) * 15)) / (15 * unitTotal)

        # Set the GUI text to the variable for out GPA variable, round to three decimal places
        self.gpaResult.configure(text=str(round(gpaScore, 3)))

        # Set the WAM gui text to the result
        #self.wamResult.configure(text=str(wamScore))

        self.statsGPA.configure(text=str(gpaScore))
        self.statsWAM.configure(text=str(wamScore))

    # Method is responsible for saving the students information to a file
    def saveFile(self):
        print('File saved!')
        self.saveLabel.configure(text='file saved')


# Create an instance of the gpa calculator
gui = GPA_Calculator()
