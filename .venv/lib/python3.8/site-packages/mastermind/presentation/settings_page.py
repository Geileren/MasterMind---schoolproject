#!/usr/bin/env python

# built-in imports
import tkinter as tk
# local imports


class SettingsMenuPage(tk.Frame):
    def __init__(self, main=None):
        super().__init__(main)
        self.main = main
        self.draw_widget()

    def draw_widget(self):
        pass