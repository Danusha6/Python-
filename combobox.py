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