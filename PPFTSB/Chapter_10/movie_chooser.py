'''
Created on Apr 28, 2016

@author: robisoc
'''
# Movie Chooser
# Demonstrates check buttons

from tkinter import *
class Application(Frame):
    """ GUI Application for favorite movie types. """
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgents()
        
    def create_widgets(self):
        """ Create widgets for movie type choices. """
        # create description label
        Label(self,
              text = "Choose your favorite movie types"
              ).grid(row = 0, column = 0, sticky = W)
              