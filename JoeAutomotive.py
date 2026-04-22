# Name: Ariana Fafach
# Date: 4/22/2026
# Title: Program #2: Joe's Automotive

# Joe's Automotive performs the following routine maintenance service:
# Oil Change - $30.00
# Lube Job - $20.00
# Radiator Flush - $40.00
# Transmission Fluid - $100.00
# Inspection - $35.00
# Muffler replacement - $200.00
# Tire Rotation - $20.00
# Write a GUI with check buttons that allows the user to select any or all of these services.  When the user clicks a button, the total charges should be displayed.


import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Creat main window:
        self.main_window = tkinter.Tk()
        # Name main window:
        self.main_window.title("Joe's Automotive Service Options")

        # Creat three frames, the top one for the instructions, the middle one for the checkbuttons, and the third one for the buttons:
        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)

        # Display the instructions in the top frame:
        self.main_label = tkinter.Label(self.frame1, text = "Please select the services that you would like done:")

        # Pack the instructions:
        self.main_label.pack()

        # Create 7 IntVar objects to use with the checkbuttons:
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()

        # Set all of the checkboxes a unchecked:
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)
        
        # Creat all of the checkbuttons and put them in the middle frame, also line them all up evenly:
        self.cb1 = tkinter.Checkbutton(self.frame2, text = "Oil Change - $30.00", variable = self.cb_var1, anchor = "w")
        self.cb2 = tkinter.Checkbutton(self.frame2, text = "Lube Job - $20.00", variable = self.cb_var2, anchor = "w")
        self.cb3 = tkinter.Checkbutton(self.frame2, text = "Radiator Flush - $40.00", variable = self.cb_var3, anchor = "w")
        self.cb4 = tkinter.Checkbutton(self.frame2, text = "Transmission Fluid - $100.00", variable = self.cb_var4, anchor = "w")
        self.cb5 = tkinter.Checkbutton(self.frame2, text = "Inspection - $35.00", variable = self.cb_var5, anchor = "w")
        self.cb6 = tkinter.Checkbutton(self.frame2, text = "Muffler replacement - $200.00", variable = self.cb_var6, anchor = "w")
        self.cb7 = tkinter.Checkbutton(self.frame2, text = "Tire Rotation - $20.00", variable = self.cb_var7, anchor = "w")

        # Pack the checkboxes:
        self.cb1.pack(fill = "x", padx = 10)
        self.cb2.pack(fill = "x", padx = 10)
        self.cb3.pack(fill = "x", padx = 10)
        self.cb4.pack(fill = "x", padx = 10)
        self.cb5.pack(fill = "x", padx = 10)
        self.cb6.pack(fill = "x", padx = 10)
        self.cb7.pack(fill = "x", padx = 10)

        # Creat a "add button" and a quit button:
        self.add_button = tkinter.Button(self.frame2, text = "Get total cost", command = self.add_costs)
        self.quit_button = tkinter.Button(self.frame2, text = "Quit", command = self.main_window.destroy)

        # Pack the buttons:
        self.add_button.pack()
        self.quit_button.pack()

        # Pack the frames:
        self.frame1.pack(padx = 40, pady = 5)
        self.frame2.pack()
        self.frame3.pack()

        tkinter.mainloop()

    def add_costs(self):   
        # Initialize the total_value variable at 0
        total_value = 0.0

        # Add up the prices of whatever buttons the user checks:
        if self.cb_var1.get() == 1:
            total_value += 30.00
        if self.cb_var2.get()  == 1:
            total_value += 20.00
        if self.cb_var3.get()  == 1:
            total_value += 40.00
        if self.cb_var4.get()  == 1:
            total_value += 100.00
        if self.cb_var5.get()  == 1:
            total_value += 35.00
        if self.cb_var6.get()  == 1:
            total_value += 200.00
        if self.cb_var7.get()  == 1:
            total_value += 20.00
        
        # Creat a messagebox that displays the total price:
        tkinter.messagebox.showinfo("Total Price", f"Your total cost will be ${total_value}.")

# Creat an instance of MyGUI:
if __name__ == "__main__":
    mygui = MyGUI()
