#!/usr/bin/env python

# built-in imports
import tkinter as tk
import sys

# local imports
from mastermind.presentation.settings_page import SettingsMenuPage
from mastermind.presentation.saves_menu import SavesMenuPage


class GameMenuPage(tk.Frame):
    def __init__(self, main=None):
        super().__init__(main)
        self.main = main
        self.draw_widget()
        self.main.geometry('500x500')
        self.config(bg="#2E3440")
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)

    def draw_widget(self):

        self.frame = tk.Frame(self, bg="#2E3440")
        self.frame.grid(column=1, row=1)

        self.new_game_button = tk.Button(self.frame, text="Start et nyt spil", command=self.new_game, bg="#434C5E", fg="#8fbcbb", width=20)
        self.new_game_button.grid(column=1, row=1)

        self.load_game_button = tk.Button(self.frame, text="Genindlæs et gemt spil", bg="#434C5E", fg="#8fbcbb", command=self.load_save, width=20, state="disabled")
        self.load_game_button.grid(column=1, row=2)
        

        self.end_button = tk.Button(self.frame, text="Afslut program", command=sys.exit, width=20, bg="#434C5E", fg="#8fbcbb")
        self.end_button.grid(column=1, row=3)

        self.error_label = tk.Label(self.frame, text="Genindlæsning af spil vil blive tilføjet i en senere version", bg="#2E3440", fg="#8fbcbb")
        self.error_label.grid(column=1, row=4)

    def new_game(self):
        SettingsMenuPage(self.main).grid(column=1, row=1, sticky="NEWS")

    def load_save(self):
        SavesMenuPage(self.main).grid(column=1, row=1, sticky="NEWS")
        #self.error_label.config(text="Denne funktion er ikke implementeret endnu")