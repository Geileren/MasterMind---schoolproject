#!/usr/bin/env python

# built-in imports
import tkinter as tk
# local imports
from mastermind.presentation.components.saves_icon import Save_icon

class SavesMenuPage(tk.Frame):
    def __init__(self, main=None):
        super().__init__(main)
        self.main = main
        self.draw_widget()
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)



    def draw_widget(self):

        self.frame = tk.Frame(self)
        self.frame.grid(column=1, row=1)

        for i in range(3):
            Save_icon(self.frame, i+1, column=i+1, row=1)