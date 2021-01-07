#!/usr/bin/env python

# built-in imports
import tkinter as tk

# local imports
from mastermind.presentation.menu_page import GameMenuPage


class MainApp(tk.Frame):
    def __init__(self, main=None):
        super().__init__(main)
        self.main = main
        self.draw_widget()

    def draw_widget(self):
        GameMenuPage().grid(sticky='NEWS')


def main():
    root = tk.Tk()
    MainApp(main=root)
    root.mainloop()

if __name__ == '__main__':
    main()