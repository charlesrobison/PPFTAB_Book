# Simple GUI
# Demonstrates creating a window

from tkinter import *
from logging import root

# Create the root window
root = Tk()

# Modify the window
root.title("Simple GUI")
root.geometry("200x100")

# Kick off the window's event loop.
root.mainloop()
