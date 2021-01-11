#!/usr/bin/env python

# built-in imports
import tkinter as tk
import time
# local imports


class GameMenuPage(tk.Frame):
    def __init__(self, main=None):
        super().__init__(main)
        self.main = main
        self.draw_widget()


