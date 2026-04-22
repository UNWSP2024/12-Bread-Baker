# Name: Ariana Fafach
# Date: 4/22/2026
# Title: Program #3 Long-Distance Calls


import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Creat main window:
        self.main_window = tkinter.Tk()
        # Name main window:
        self.main_window.title("Rate Category: Rate per Minute")

        # Create three frames, the top one for the radio buttons, the middle one for the label and entry widget, and the bottom one for the buttons:
        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)

        # Pack frames with padding:
        self.frame1.pack(padx = 25, pady = 5)
        self.frame2.pack(padx = 10, pady = 5)
        self.frame3.pack(padx = 10, pady = 5)

        # Creat a IntVar variable to use with the radiobuttons:
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        # Creat the Radiobuttons:
        self.radbtn1 = tkinter.Radiobutton(self.frame1, text = "Daytime (6:00 A.M. through 5:59 P.M.) 	$0.02", variable = self.radio_var, value = 1)
        self.radbtn2 = tkinter.Radiobutton(self.frame1, text = "Evening (6:00 P.M.  through 11:59 P.M.)	$0.12", variable = self.radio_var, value = 2)
        self.radbtn3 = tkinter.Radiobutton(self.frame1, text = "Off-Peak (midnight through 5:59 P.M.) 	$0.05", variable = self.radio_var, value = 3)

        # Pack the buttons:
        self.radbtn1.pack()
        self.radbtn2.pack()
        self.radbtn3.pack()

        # Creat the label and the entry widget:
        self.label = tkinter.Label(self.frame2, text = "Enter the number of minutes of your call:")
        self.minute_entry = tkinter.Entry(self.frame2, width = 10)

        # Pack the label and entry widget so they are side by side:
        self.label.pack(side = "left")
        self.minute_entry.pack(side = "right")
        
        # Create a buttons to see the charge and a button to quit:
        self.charge_button = tkinter.Button(self.frame3, text = "See total charge", command = self.calculate)
        self.quit_button = tkinter.Button(self.frame3, text = "Quit", command = self.main_window.destroy)

        # Pack the buttons:
        self.charge_button.pack(side = "left")
        self.quit_button.pack(side = "right")

        tkinter.mainloop()

    def calculate(self):

        # See which radio button is selected and calculate the price accordingly:
        if self.radio_var.get() == 1:
            charge = float(self.minute_entry.get()) * 0.02
        elif self.radio_var.get() == 2:
            charge = float(self.minute_entry.get()) * 0.12
        elif self.radio_var.get() == 3:
            charge = float(self.minute_entry.get()) * 0.05

        # Display the total price in a showinfo window:
        tkinter.messagebox.showinfo("Total Price", f"The total price for that call will be ${charge}")

# Create an instance of MyGUI:
if __name__ == "__main__":

    mygui = MyGUI()