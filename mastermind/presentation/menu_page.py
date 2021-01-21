#!/usr/bin/env python

# built-in imports
import tkinter as tk
# local imports
from mastermind.presentation.settings_page import SettingsMenuPage

class GameMenuPage(tk.Frame):
    def __init__(self, main=None):
        super().__init__(main)
        self.main = main
        self.draw_widget()
        self.main.geometry('500x500')
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)



    def draw_widget(self):

        self.frame = tk.Frame(self)
        self.frame.grid(column=1, row=1)

        self.new_game_button = tk.Button(self.frame, text="Start et nyt spil", command=self.new_game)
        self.new_game_button.grid(column=1, row=1)

        self.load_game_button = tk.Button(self.frame, text="Genindlæs et gemt spil")
        self.load_game_button.grid(column=1, row=2)

        self.error_label = tk.Label(self.frame)
        self.error_label.grid(column=1, row=3)



    def new_game(self):
        SettingsMenuPage(self.main).grid(column=1, row=1, sticky="NEWS")