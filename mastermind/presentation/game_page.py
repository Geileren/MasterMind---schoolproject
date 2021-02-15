#!/usr/bin/env python

# built-in imports
import tkinter as tk

# local imports
#from mastermind.logic.logic import


class GameButton():
    def __init__(self, root, x, y, parent):
        self.root = root
        self.x = x
        self.y = y
        self.parent = parent
        self.button = tk.Button(self.root, width=5, height=2, command=self.but_press)
        self.button.grid(column=self.x, row=self.y)

    def but_press(self):
        if self.parent == "clear":
            pass
        else:
            self.button.config(bg=self.parent.colormode)


class ColorButton():
    def __init__(self, root, x, y, color, parent):
        self.root = root
        self.x = x
        self.y = y
        self.color = color
        self.parent = parent

        self.button = tk.Button(self.root, width=5, height=2, bg=self.color, command=self.but_press)
        self.button.grid(column=self.x, row=self.y)

    def but_press(self):
        self.parent.colormode = self.color

class GamePage(tk.Frame):
    def __init__(self, main=None):
        super().__init__(main)
        self.main = main
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        self.buttons = []
        self.colormode = "clear"


        self.draw_widget()



    def draw_widget(self):

        self.frame = tk.Frame(self)
        self.frame.grid(column=1, row=1)



        for x in range(4):
            for y in range(12):
                self.buttons.append(GameButton(self.frame, x, y, self))

        ColorButton(self.frame, 5, 2, "red", self)
        ColorButton(self.frame, 5, 1, "blue", self)



    def color_press(self):
        pass

