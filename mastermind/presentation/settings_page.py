#!/usr/bin/env python

# built-in imports
import tkinter as tk
# local imports
from mastermind.presentation.game_page import GamePage
from mastermind.presentation.code_type_page import CodeInputPage

class SettingsMenuPage(tk.Frame):
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

        # Galaxy brain settings widgets and vars
        self.galaxy_label = tk.Label(self.frame, text="Galaxy Brain sværhedsgrad")
        self.galaxy_label.grid(column=1, row=1)

        self.galaxy_var = tk.IntVar()
        self.galaxy_chech = tk.Checkbutton(self.frame, variable=self.galaxy_var)
        self.galaxy_chech.grid(column=2, row=1)


        # Code settings widgets and vars
        self.code_var = tk.IntVar()

        self.auto_code_text = tk.Label(self.frame, text="Benyt en automatisk genereret kode")
        self.auto_code_text.grid(column=1, row=2)

        self.type_code_text = tk.Label(self.frame, text="Indtast egen kode")
        self.type_code_text.grid(column=2, row=2)

        self.auto_code_radio = tk.Radiobutton(self.frame, variable=self.code_var, value=0)
        self.auto_code_radio.grid(column=1, row=3)

        self.type_code_radio = tk.Radiobutton(self.frame, variable=self.code_var, value=1)
        self.type_code_radio.grid(column=2, row=3)

        self.code_var.set(1)

        # Multi color settings and vars
        self.multi_color_var = tk.IntVar()

        self.multi_color_text = tk.Label(self.frame, text="Den samme farve må optræde flere gange i koden")
        self.multi_color_text.grid(column=1, row=4)

        self.multi_color_check = tk.Checkbutton(self.frame, variable=self.multi_color_var)
        self.multi_color_check.grid(column=2, row=4)

        self.start_button = tk.Button(self.frame, text="Start spil", command=self.start)
        self.start_button.grid(column=1, row=5)

    def start(self):
        # needs logic-layer functions


        if self.code_var.get() == 0:
            pass
        else:
            CodeInputPage(self.main).grid(column=1, row=1, sticky="NEWS")


        #print(self.multi_color_var.get())

        #print(self.galaxy_var.get())
