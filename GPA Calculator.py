"""
Grade Point Average Calculator by Liam Andrews
Version : 0.3

"""

import tkinter

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

        # Strings that grades will be entered into via entry boxes in the GUI
        self.entry1String = tkinter.StringVar()
        self.entry2String = tkinter.StringVar()
        self.entry3String = tkinter.StringVar()
        self.entry4String = tkinter.StringVar()


        # Instructions for the user, displayed as a label with appropriate padding
        instructionLabel = tkinter.Label(self.main, text ='Enter your final grade for each of your four classes')
        instructionLabel.pack(pady = 10)

        # Result 1 label
        resultLabel1 = tkinter.Label(self.main, text='Class 1: ')
        resultLabel1.pack()
        # Empty text box for entering data
        resultEntry1 = tkinter.Entry(self.main, textvariable=self.entry1String)
        resultEntry1.pack()

        # Result 2 label
        resultLabel2 = tkinter.Label(self.main, text='Class 2: ')
        resultLabel2.pack()
        # Empty text box for entering data
        resultEntry2 = tkinter.Entry(self.main, textvariable=self.entry2String)
        resultEntry2.pack()

        # Result 3 label
        resultLabel1 = tkinter.Label(self.main, text='Class 3: ')
        resultLabel1.pack()
        # Empty text box for entering data
        resultEntry3 = tkinter.Entry(self.main, textvariable=self.entry3String)
        resultEntry3.pack()

        # Result 4 label
        resultLabel1 = tkinter.Label(self.main, text='Class 4: ')
        resultLabel1.pack()
        # Empty text box for entering data
        resultEntry4 = tkinter.Entry(self.main, textvariable=self.entry4String)
        resultEntry4.pack()

        # Button to calculate the GPA
        calculateButton = tkinter.Button(self.main, text='Calculate GPA', command = self.calculateGPA)
        calculateButton.pack(pady=20)

        # Contains the frame with the GPA result
        resultsFrame = tkinter.Frame(self.main)
        resultsFrame.pack()
        gpaLabel = tkinter.Label(resultsFrame, text= 'Your GPA is: ')
        gpaLabel.pack(side = 'left')
        self.gpaResult = tkinter.Label(resultsFrame, text ='0')
        self.gpaResult.pack(side = 'right')



        # Enter main loop of program
        self.main.mainloop()

    # Calculates and displays GPA via the GUI, once button is pressed
    def calculateGPA(self):
        # Create default value to print if no score recorded, create empty list for the grades to be entered into
        gpaScore = 0.0
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

        # Calculation for GPA
        gpaScore = gpaScore / (15 * 4)


        # Set the GUI text to the variable for out GPA variable
        self.gpaResult.configure(text=str(gpaScore))


# Create an instance of the gpa calculator
gui = GPA_Calculator()
