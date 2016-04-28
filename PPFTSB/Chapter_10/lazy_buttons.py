'''
Created on Apr 27, 2016

@author: robisoc
'''
# Lazy Buttons
# Demonstrates creating buttons

from tkinter import *

# Create a root window.
root = Tk()
root.title("Lazy Buttons")
root.geometry("200x85")

#Create a frame in the window to hold other widgets.
app = Frame(root)
app.grid()

# Create a button in the frame.
bttn1 = Button(app, text = "I do nothing!")
bttn1.grid()

# Create a second button in the frame.
bttn2 = Button(app)
bttn2.grid()

bttn2.configure(text = "Me too!")

# Create a third button in the frame.
bttn3 = Button(app)
bttn3.grid()

bttn3["text"] = "Same here!"

# Kick off the window's event loop.
root.mainloop()