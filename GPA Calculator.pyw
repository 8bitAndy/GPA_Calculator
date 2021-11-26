"""
Grade Point Average Calculator by Liam Andrews
Version : 0.3

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
        self.main.geometry('500x300')
        # Change the window's icon
        self.main.iconbitmap('icon.ico')
        # Prevent window resizing
        self.main.resizable(0,0)

        # Creating the tabs for the GUI, essentially two frames, either hidden or shown by using the tabs at the top of GUI
        tabControl = ttk.Notebook(self.main)
        gpaTab = tkinter.Frame(tabControl)
        statsTab = tkinter.Frame(tabControl)
        fileTab = tkinter.Frame(tabControl)

        # Label the two tabs appropriatly
        tabControl.add(gpaTab, text='GPA Calculator')
        tabControl.add(statsTab, text='View Statistics')
        tabControl.add(fileTab, text='Save files')

        # Packing the tabs and expanding it to the entire window
        tabControl.pack(expand = True, fill="both")


        """
        WAM/GPA Calculator tab
        """

        # Strings that grades will be entered into via entry boxes in the GUI
        self.entry1String = tkinter.StringVar()
        self.entry2String = tkinter.StringVar()
        self.entry3String = tkinter.StringVar()
        self.entry4String = tkinter.StringVar()


        # Instructions for the user, displayed as a label with appropriate padding
        instructionLabel = tkinter.Label(gpaTab, text ='Enter your final mark for each of your four classes')
        instructionLabel.pack(pady = 10)

        # Result 1 label
        resultLabel1 = tkinter.Label(gpaTab, text='Class 1: ')
        resultLabel1.pack()
        # Empty text box for entering data
        resultEntry1 = tkinter.Entry(gpaTab, textvariable=self.entry1String)
        resultEntry1.pack()

        # Result 2 label
        resultLabel2 = tkinter.Label(gpaTab, text='Class 2: ')
        resultLabel2.pack()
        # Empty text box for entering data
        resultEntry2 = tkinter.Entry(gpaTab, textvariable=self.entry2String)
        resultEntry2.pack()

        # Result 3 label
        resultLabel1 = tkinter.Label(gpaTab, text='Class 3: ')
        resultLabel1.pack()
        # Empty text box for entering data
        resultEntry3 = tkinter.Entry(gpaTab, textvariable=self.entry3String)
        resultEntry3.pack()

        # Result 4 label
        resultLabel1 = tkinter.Label(gpaTab, text='Class 4: ')
        resultLabel1.pack()
        # Empty text box for entering data
        resultEntry4 = tkinter.Entry(gpaTab, textvariable=self.entry4String)
        resultEntry4.pack()

        # Button to calculate the GPA
        calculateButton = tkinter.Button(gpaTab, text='Calculate results', command = self.calculateGPA)
        calculateButton.pack(pady = 10)

        # Contains the frame with the GPA result
        resultsFrame = tkinter.Frame(gpaTab)
        resultsFrame.pack()

        # Display for GPA within the results frame
        gpaFrame = tkinter.Frame(resultsFrame)
        gpaFrame.pack(side='left')
        gpaLabel = tkinter.Label(gpaFrame, text= 'Your GPA is: ')
        gpaLabel.pack(side = 'left')
        self.gpaResult = tkinter.Label(gpaFrame, text ='0')
        self.gpaResult.pack(side = 'right')

        # Display the WAM within the results frame
        wamFrame = tkinter.Frame(resultsFrame)
        wamFrame.pack(side='right')
        gpaLabel = tkinter.Label(wamFrame, text= 'Your WAM is: ')
        gpaLabel.pack(side='left')
        self.wamResult = tkinter.Label(wamFrame, text ='0')
        self.wamResult.pack(side='right')

        # Stats tab gpa label
        self.statsGPA = tkinter.Label(statsTab, text= '0')
        self.statsGPA.pack()
        # stats tab wam label
        self.statsWAM = tkinter.Label(statsTab, text= '0')
        self.statsWAM.pack()


        """
        File handling tab
        """

        # Button to save information to a file
        saveButton = tkinter.Button(fileTab, text='Save file', command = self.saveFile)
        saveButton.pack(pady = 20)

        # Label to display notification if file has saved or not
        self.saveLabel = tkinter.Label(fileTab, text= '')
        self.saveLabel.pack()


        # Enter main loop of program
        self.main.mainloop()

    # Calculates and displays GPA via the GUI, once button is pressed
    def calculateGPA(self):
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
        wamScore = wamScore  / (15 * 4)

        # Set the GUI text to the variable for out GPA variable
        self.gpaResult.configure(text=str(gpaScore))

        # Set the WAM gui text to the result
        self.wamResult.configure(text=str(wamScore))

        self.statsGPA.configure(text=str(gpaScore))
        self.statsWAM.configure(text=str(wamScore))


    # Method is responsible for saving the students information to a file
    def saveFile(self):
        print('File saved!')
        self.saveLabel.configure(text= 'file saved')


# Create an instance of the gpa calculator
gui = GPA_Calculator()
