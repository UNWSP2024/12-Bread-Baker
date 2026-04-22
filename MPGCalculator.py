# Name: Ariana Fafach
# Date: 4/22/2026
# Title: Program #1: MPG Calculator

import tkinter
import tkinter.messagebox

class MyGUI:

    def __init__ (self):
        # Create the main window widget:
        self.main_window = tkinter.Tk()
        self.main_window.title("MPG Calculator")

        # Create three frames:
        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)

        # Create the first label and the first entry widget and put them in the first frame:
        self.label1 = tkinter.Label(self.frame1, text = "Enter the number of gallons that your car holds: ")
        self.gallon_entry = tkinter.Entry(self.frame1, width = 10)

        # Creat the second label and the second entry widget and put them into the second frame:
        self.label2 = tkinter.Label(self.frame2, text = "Enter the number of miles that your car can be driven on a full tank: " )
        self.miles_entry = tkinter.Entry(self.frame2, width = 10)

        # Create two buttons, a "Calculate" button and a quit button and put them into the third frame:
        self.calculate_button = tkinter.Button(self.frame3, text ='Calculate', command = self.calculate)
        self.quit_button = tkinter.Button(self.frame3, text = 'Quit', command = self.main_window.destroy)

        # Pack the Entry widgets to the right of the labels:
        self.gallon_entry.pack(side = 'right')
        self.miles_entry.pack(side = 'right')

        # Pack the buttons side by side:
        self.calculate_button.pack(side = 'left')
        self.quit_button.pack(side = 'right')

        # Pack the labels:
        self.label1.pack()
        self.label2.pack()

        # Pack the frames with external padding:
        self.frame1.pack(padx = 5, pady = 5)
        self.frame2.pack(padx = 10, pady = 0)
        self.frame3.pack(padx = 5, pady = 5)
    
        tkinter.mainloop()

    # Function calculates and displays the miles per gallon:
    def calculate(self):

        gallons = float(self.gallon_entry.get())
        miles = float(self.miles_entry.get())

        MPG = miles/gallons

        tkinter.messagebox.showinfo('Results', f"Your car can be driven {MPG} miles per gallon.")

# Create an instance of the MyGUI class:

if __name__ == "__main__":
    mygui = MyGUI()
