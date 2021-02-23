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
        self.config(bg="#2E3440")
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)

    def draw_widget(self):

        # Overall frame
        self.frame = tk.Frame(self, bg="#2E3440")
        self.frame.grid(column=1, row=1)

        # Galaxy brain settings widgets and vars
        self.galaxy_label = tk.Label(self.frame, text="Galaxy Brain sværhedsgrad", bg="#2E3440")
        self.galaxy_label.grid(column=1, row=1)

        self.galaxy_var = tk.IntVar()
        self.galaxy_chech = tk.Checkbutton(self.frame, variable=self.galaxy_var, bg="#2E3440")
        self.galaxy_chech.grid(column=2, row=1)

        # Code settings widgets and vars
        self.code_var = tk.IntVar()

        self.auto_code_text = tk.Label(self.frame, text="Benyt en automatisk genereret kode", bg="#2E3440")
        self.auto_code_text.grid(column=1, row=2)

        self.type_code_text = tk.Label(self.frame, text="Indtast egen kode", bg="#2E3440")
        self.type_code_text.grid(column=2, row=2)

        self.auto_code_radio = tk.Radiobutton(self.frame, variable=self.code_var, value=0, bg="#2E3440")
        self.auto_code_radio.grid(column=1, row=3)

        self.type_code_radio = tk.Radiobutton(self.frame, variable=self.code_var, value=1, bg="#2E3440")
        self.type_code_radio.grid(column=2, row=3)

        self.code_var.set(1)

        # Multi color settings and vars
        self.multi_color_var = tk.IntVar()

        self.multi_color_text = tk.Label(self.frame, text="Den samme farve må optræde flere gange i koden", bg="#2E3440")
        self.multi_color_text.grid(column=1, row=4)

        self.multi_color_check = tk.Checkbutton(self.frame, variable=self.multi_color_var, bg="#2E3440")
        self.multi_color_check.grid(column=2, row=4)

        # Start Button
        self.start_button = tk.Button(self.frame, text="Start spil", command=self.start, bg="#434C5E")
        self.start_button.grid(column=1, row=5)

    def start(self):
        # needs logic-layer functions

        if self.code_var.get() == 0:
            GamePage(self.main).grid(column=1, row=1, sticky="NEWS")
        else:
            CodeInputPage(self.main).grid(column=1, row=1, sticky="NEWS")


