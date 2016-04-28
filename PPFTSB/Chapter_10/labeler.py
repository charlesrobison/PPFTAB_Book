# Labeler
# Demonstrates a label

from tkinter import *

# Create the root window.
root = Tk()
root.title("Labeler")
root.geometry("200x50")

# Create a frame in the window to hold other widgets.
app = Frame(root)

app.grid()

# Create a label in the frame.
lbl = Label(app, text = "I'm a label!")

lbl.grid()

# Kick off the window's event loop.
root.mainloop()