#!/usr/bin/env python

# built-in imports
import tkinter as tk
# local imports
from mastermind.presentation.game_page import GamePage

class CodeInputPage(tk.Frame):
    def __init__(self, main=None):
        super().__init__(main)
        self.main = main
        self.draw_widget()
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)



    def draw_widget(self):

        # Overall frame
        self.frame = tk.Frame(self)
        self.frame.grid(column=1, row=1)