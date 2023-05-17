#Import the class library tkinter
import tkinter as tk

#Create a function that return an output
def button_click():
    print("Button clicked!")

#Create a function that give title to the page
root = tk.Tk()
root.title("Button Example")    


#Create an object with three parameter
button =  tk.Button(root, text="Press it!", command=button_click)
button.pack()

#Create a mainloop to keep the rook window open
root.mainloop()


