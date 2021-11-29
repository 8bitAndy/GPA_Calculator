"""
Grade Point Average Calculator by Liam Andrews
Version: 0.5
29/11/2021

 - Next version: 0.55

Need to change this new version to be more like the draft version, where it asks how many of each grade you have

TODO:
- Add settings tab
- Add ability to save results


WORKING ON CURRENTLY
    - NONE

DONE
    - Change way program calculates GPA, change interface on main tab
    - Add tab for WAM
    - Add clear button for GPA tab
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
        instructionLabel = tkinter.Label(gpaTab, text='Enter the total number of units for each grade: ')
        instructionLabel.pack(pady=10)

        # Result 1 label
        resultLabel1 = tkinter.Label(gpaTab, text='High Distinction: ')
        resultLabel1.pack()
        # Empty text box for entering data, justify right is used to make text appear centred
        self.resultEntry1 = tkinter.Entry(gpaTab, textvariable=self.entry1String, justify='center')
        self.resultEntry1.pack()

        # Result 2 label
        resultLabel2 = tkinter.Label(gpaTab, text='Distinction: ')
        resultLabel2.pack()
        # Empty text box for entering data, justify right is used to make text appear centred
        self.resultEntry2 = tkinter.Entry(gpaTab, textvariable=self.entry2String, justify='center')
        self.resultEntry2.pack()

        # Result 3 label
        resultLabel3 = tkinter.Label(gpaTab, text='Credit: ')
        resultLabel3.pack()
        # Empty text box for entering data, justify right is used to make text appear centred
        self.resultEntry3 = tkinter.Entry(gpaTab, textvariable=self.entry3String, justify='center')
        self.resultEntry3.pack()

        # Result 4 label
        resultLabel4 = tkinter.Label(gpaTab, text='Pass: ')
        resultLabel4.pack()
        # Empty text box for entering data, justify right is used to make text appear centred
        self.resultEntry4 = tkinter.Entry(gpaTab, textvariable=self.entry4String, justify='center')
        self.resultEntry4.pack()

        # Result 5 label
        resultLabel5 = tkinter.Label(gpaTab, text='Fail: ')
        resultLabel5.pack()
        # Empty text box for entering data, justify right is used to make text appear centred
        self.resultEntry5 = tkinter.Entry(gpaTab, textvariable=self.entry5String, justify='center')
        self.resultEntry5.pack()


        # Frame for calculate GPA button and clear button
        buttonFrame = tkinter.Frame(gpaTab)
        buttonFrame.pack(pady=15)

        # Button to calculate the GPA, is packed into buttonFrame
        calculateButton = tkinter.Button(buttonFrame, text='Calculate results', command=self.calculateGPA)
        calculateButton.pack(side='left', padx=5)

        # Button to clear all entry fields, is packed into buttonFrame
        clearButton = tkinter.Button(buttonFrame, text='Clear', command=self.clearEntryFields)
        clearButton.pack(side='right')

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

        # Stats tab gpa label
        self.statsGPA = tkinter.Label(statsTab, text='0')
        self.statsGPA.pack()

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

        # Extract the input from all 5 entry boxes, converts all values to ints.
        # Exception handling deals with any empty entry fields, will assign a value of zero if no value is given.
        try:
            hd_grades = int(self.entry1String.get())
        except ValueError:
            hd_grades = 0

        try:
            d_grades = int(self.entry2String.get())
        except ValueError:
            d_grades = 0

        try:
            cr_grades = int(self.entry3String.get())
        except ValueError:
            cr_grades = 0

        try:
            p_grades = int(self.entry4String.get())
        except ValueError:
            p_grades = 0

        try:
            fail_grades = int(self.entry5String.get())
        except ValueError:
            fail_grades = 0


        # Calculate the total number units taken. Used in calculation for GPA
        unitTotal = hd_grades + d_grades + cr_grades + p_grades + fail_grades


        # Create default value to print if no score recorded
        gpaScore = 0.0

        gpaScore = 0


        """
            --- FORMULA TO CALCULATE GPA ---
            Multiply amount of each grade by 15 points to get GPA, then divide by total amount of units.
            Will only execute if a valid number of units has been entered. Doing this prevents the program
            attempting to divide by zero or a negative number.
        """
        if unitTotal != 0 and unitTotal > 0:
            gpaScore = (((hd_grades * 4) * 15) + ((d_grades * 3.5) * 15) + ((cr_grades * 3) * 15) + ((p_grades * 2) * 15) + ((fail_grades * 0) * 15)) / (15 * unitTotal)

        # Set the GUI text to the variable for out GPA variable, round to three decimal places
        self.gpaResult.configure(text=str(round(gpaScore, 3)))


    # Clear all entry text fields, sets GPA back to zero
    def clearEntryFields(self):
        # Deletes string in entry from index zero to the last value
        self.resultEntry1.delete(0, 'end')
        self.resultEntry2.delete(0, 'end')
        self.resultEntry3.delete(0, 'end')
        self.resultEntry4.delete(0, 'end')
        self.resultEntry5.delete(0, 'end')

        self.gpaResult.configure(text='0')


    # Method is responsible for saving the students information to a file
    def saveFile(self):
        print('File saved!')
        self.saveLabel.configure(text='file saved')


# Create an instance of the gpa calculator
gui = GPA_Calculator()
