#!/usr/bin/env python

# built-in imports
import tkinter as tk
# local imports


class GameMenuPage(tk.Frame):
    def __init__(self, main=None):
        super().__init__(main)
        self.main = main
        self.draw_widget()
        self.main.geometry('500x500')



    def draw_widget(self):

        self.new_game_button = tk.Button(self, text="Start et nyt spil")
        self.new_game_button.grid(column=1, row=1, sticky="N")

        self.load_game_button = tk.Button(self, text="Genindlæs et gemt spil")
        self.load_game_button.grid(column=1, row=2)

        self.error_label = tk.Label(self)
        self.error_label.grid(column=1, row=3)


