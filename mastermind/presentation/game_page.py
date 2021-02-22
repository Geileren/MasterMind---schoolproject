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
        self.button = tk.Button(self.root, width=5, height=2, command=self.but_press, state="disabled")
        self.button.grid(column=self.x, row=self.y)
        self.color = ""

    def but_press(self):
        if self.parent.colormode == "clear":
            pass
        else:
            self.color = self.parent.colormode
            self.button.config(bg=self.color)
            print(self.color)


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
        self.main.geometry("500x600")
        self.config(bg="#2E3440")
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        self.colormode = "clear"
        self.colormode_status = False
        self.current_row = 0

        self.draw_widget()
        self.unlock_row()

    def draw_widget(self):

        self.frame = tk.Frame(self)
        self.frame.grid(column=1, row=1, sticky="SW")

        self.color_frame = tk.Frame(self, highlightbackground="black", highlightthickness=2)
        self.color_frame.grid(column=0, row=1, padx=(20,0), pady=10, sticky="SE")

        self.buttons = [GameButton(self.frame, x, y, self) for y in range(12) for x in range(4)]

        self.color_buttons = [ColorButton(self.color_frame, i // 4, i % 4, j, self) for i, j in enumerate(color_list)]

        self.next_round_button = tk.Button(self, text="Næste Runde", command=self.lock_round)
        self.next_round_button.grid(column=2, row=1, sticky="S", padx=10, pady=10)

    def clear_color_mode(self):
        if self.colormode_status == True:
            self.colormode = "clear"
            self.colormode_status = False
            for i in self.color_buttons:
                i.button.config(relief="raised")

    def unlock_row(self):
        self.current_row += 1
        for i in self.buttons[len(self.buttons)-4*self.current_row:len(self.buttons)-4*(self.current_row-1)]:
            i.button.config(state="normal")

    def lock_row(self):
        for i in self.buttons[len(self.buttons)-4*self.current_row:len(self.buttons)-4*(self.current_row-1)]:
            i.button.config(state="disabled")

    def save_row(self):
        self.saved_codes = [i.color for i in self.buttons[len(self.buttons) - 4 * self.current_row:len(self.buttons) - 4 * (self.current_row - 1)]]
        print(self.saved_codes)

    def lock_round(self):
        self.lock_row()
        self.save_row()
        self.unlock_row()