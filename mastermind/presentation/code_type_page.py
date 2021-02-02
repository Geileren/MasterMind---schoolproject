#!/usr/bin/env python

# built-in imports
import tkinter as tk
# local imports
from mastermind.presentation.game_page import GamePage

class CodeInputPage(tk.Frame):
    def __init__(self, main=None):
        super().__init__(main)
        self.main = main
        self.config(bg="#4c566a")
        self.draw_widget()
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)



    def draw_widget(self):

        # Overall frame
        self.frame = tk.Frame(self, bg="#4c566a")
        self.frame.grid(column=1, row=1)

        self.start_but = tk.Button(self.frame, text="Din Mor Thien", command=self.start)
        self.start_but.grid(column=1, row=1)

    def start(self):
        GamePage(self.main).grid(column=1, row=1, sticky="NEWS")