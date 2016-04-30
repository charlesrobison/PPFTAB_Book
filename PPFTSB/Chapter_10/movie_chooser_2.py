'''
Created on Apr 29, 2016

@author: robisoc
'''
# Movie Chooser 2
# Demonstrates radio buttons

from tkinter import *

class Application(Frame):
    """ GUI Application for favorite movie types. """
    def __init__(self, master):
        """ Initialize Frame. """
        Frame.__init__(self, master)
        self.grid()
        self.create_widget()
    
    def create_widgets(self):
        """ Create widgets for movie type choices. """
        # create description label
        Label(self,
              text = "Choose your favorite type of movie"
              ).grid(row = 0, column = 0, sticky = W)
        # create instruction label
        Label(self,
              text = "Select one:"
              ).grid(row = 1, column = 0, sticky = W)
              
        # create variable for single, favorite type of movie
        self.favorite = StringVar()
    
        # create Comedy radio button
        Radiobutton(self,
                    text = "Comedy",
                    variable = self.favorite,
                    value = "comedy.",
                    command = self.update_text
                    ).grid(row = 2, column = 0, sticky = W)
                
        # create Drama radio button
        Radiobutton(self,
                    text = "Drama",
                    variable = self.favorite,
                    value = "drama.",
                    command = self.update_text
                    ).grid(row = 3, column = 0, sticky = W)
                    
        # create Romance radio button
        Radiobutton(self,
                    text = "Romance",
                    variable = self.favorite,
                    value = "romance.",
                    command = self.update_text
                    ).grid(row = 4, column = 0, sticky = W)