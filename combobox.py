#import the tikinter class library
import tkinter as tk
from tkinter import ttk

#Cfreate a function with a parameter
def on_select(event):

    #Create an item object that holds the value of selected item
    selected_item = event.widget.get()
    print("Selected item:", selected_item)

#Create a function that give title to the page
root = tk.Tk()
root.title("Combobox Example") 

#Create a static array of items
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]

#Create a widget and connect it with the array
combo_box = ttk.Combobox(root, values=items)

#Bind the combobox object with an event function
combo_box.bind("<<ComboboxSelected>>", on_select)

combo_box.pack()

#This makes the root window to be open unless said so
root.mainloop()