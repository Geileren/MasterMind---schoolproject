#!/usr/bin/env python

# built-in imports
import tkinter as tk

# local imports
from mastermind.presentation.game_page import GamePage
from mastermind.presentation.code_type_page import CodeInputPage
from mastermind.data.mastermind_data import ColorCode
from mastermind.logic.mastermind_logic import MastermindLogic
from mastermind.data.mastermind_data import color_list

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

        # Frame and operational buttons
        self.but_frame = tk.Frame(self.frame)
        self.but_frame.grid(column=2, row=5)

        self.start_button = tk.Button(self.but_frame, text="Fortsæt", command=self.start, bg="#434C5E")
        self.start_button.grid(column=2, row=1)

        self.back_button = tk.Button(self.but_frame, text="Tilbage", command=self.destroy)
        self.back_button.grid(column=1, row=1)

    def start(self):
        logic = MastermindLogic()
        if self.code_var.get() == 0:
            self.destroy()
            color = ColorCode()
            if self.multi_color_var.get() == 1:
                color.make(logic.generate_code(color_list))
            else:
                color.make(logic.generate_unique_code(color_list))
            GamePage(color, self.main).grid(column=1, row=1, sticky="NEWS")
        elif self.multi_color_var.get() == 1:
            CodeInputPage(True, self.main).grid(column=1, row=1, sticky="NEWS")
            self.destroy()
        else:
            self.destroy()
            CodeInputPage(False, self.main).grid(column=1, row=1, sticky="NEWS")


