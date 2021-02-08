#!/usr/bin/env python

# built-in imports
import tkinter as tk
# local imports
from mastermind.logic.logic import color_list

class GameButton():
    def __init__(self, root, x, y, parent):
        self.root = root
        self.x = x
        self.y = y
        self.parent = parent
        self.button = tk.Button(self.root, width=5, height=2, command=self.but_press)
        self.button.grid(column=self.x, row=self.y)

    def but_press(self):
        if self.parent.colormode == "clear":
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
        if self.parent.colormode_status == False:
            self.parent.colormode_status = True
            self.parent.colormode = self.color
            self.button.config(relief="sunken")
        elif self.parent.colormode_status == True:
            if self.parent.colormode == self.color:
                self.parent.clear_color_mode()
            else:
                self.parent.clear_color_mode()
                self.parent.colormode_status = True
                self.parent.colormode = self.color
                self.button.config(relief="sunken")


class GamePage(tk.Frame):
    def __init__(self, main=None):
        super().__init__(main)
        self.main = main
        self.config(bg="#2E3440")
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        self.buttons = []
        self.color_buttons = []
        self.colormode = "clear"
        self.colormode_status = False


        self.draw_widget()



    def draw_widget(self):

        self.frame = tk.Frame(self)
        self.frame.grid(column=1, row=1, sticky="SW")

        self.color_frame = tk.Frame(self, highlightbackground="black", highlightthickness=2)
        self.color_frame.grid(column=0, row=1, padx=20, pady=10, sticky="SE")


        for x in range(4):
            for y in range(12):
                self.buttons.append(GameButton(self.frame, x, y, self))


        x_col = 0
        y_col = 0
        for i in color_list:
            self.color_buttons.append(ColorButton(self.color_frame, x_col, y_col, i, self))
            y_col += 1
            if y_col % 4 == 0:
                y_col -= 4
                x_col += 1

    def clear_color_mode(self):
        if self.colormode_status == True:
            self.colormode = "clear"
            self.colormode_status = False
            for i in self.color_buttons:
                i.button.config(relief="raised")



    def color_press(self):
        pass

