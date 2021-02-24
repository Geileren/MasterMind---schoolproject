#!/usr/bin/env python

# built-in imports
import tkinter as tk
import sys

# local imports
from mastermind.data.mastermind_data import color_list
from mastermind.logic.mastermind_logic import MastermindLogic
from mastermind.presentation.components.but_types import ColorButton, GameButton


class GamePage(tk.Frame):
    def __init__(self, color_code, main=None):
        super().__init__(main)
        self.main = main
        self.main.geometry("500x600")
        self.color_code = color_code
        print(color_code.manual_code)


        self.config(bg="#2E3440")
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)

        self.colormode = "clear"
        self.colormode_status = False

        self.current_row = 0
        self.logic = MastermindLogic()

        

        self.draw_widget()
        self.unlock_row()

    def draw_widget(self):
        

        self.frame = tk.Frame(self)
        self.frame.grid(column=1, row=1, sticky="SW")

        self.color_frame = tk.Frame(self, highlightbackground="black", highlightthickness=2)
        self.color_frame.grid(column=0, row=1, padx=(20,0), pady=10, sticky="SE")

        self.game_frame = tk.Frame(self.frame)
        self.game_frame.grid(column=1, row=0, rowspan=100)

        self.buttons = [GameButton(self.game_frame, x, y, self) for y in range(12) for x in range(4)]

        self.color_buttons = [ColorButton(self.color_frame, i // 4, i % 4, j, self) for i, j in enumerate(color_list)]

        
        self.col_indicators = []
        self.pos_indicators = []

        for i in range(12):
            self.col_indicators.append(tk.Button(self.frame, text="0", width=5, height=2, bg="white", state="disabled"))
            self.col_indicators[i].grid(column=0, row=i)

            self.pos_indicators.append(tk.Button(self.frame, text="0", width=5, height=2, bg="red", state="disabled"))
            self.pos_indicators[i].grid(column=2, row=i)

        self.next_round_button = tk.Button(self, text="Næste Runde", command=self.next_round)
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
        

    def next_round(self):
        self.lock_row()
        self.save_row()

        self.state = self.logic.check_gamestate(self.color_code.manual_code, self.saved_codes)
        print(self.state[2])

        self.pos_indicators[12 - self.current_row].config(text=str(self.state[1]))
        self.col_indicators[12 - self.current_row].config(text=str(self.state[2]))
        

        if self.state[0] == True:
            self.win()
        elif self.current_row >= 12:
            self.lose()

        self.unlock_row()

    def lose(self):
        self.root = tk.Toplevel()
        self.root.geometry("200x200")
        self.root.rowconfigure(1, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.grab_set()

        top_frame = tk.Frame(self.root)
        top_frame.grid(column=1, row=1)

        tk.Label(top_frame, text="Desvære du tabte :( \n du løb tør for runder").grid(column=1, row=1, columnspan=2)
        tk.Button(top_frame, text="Afslut", command=sys.exit).grid(column=1, row=2)
        tk.Button(top_frame, text="Gå til menuen", command=self.menu_return).grid(column=2, row=2)


    def win(self):
        self.root = tk.Toplevel()
        self.root.geometry("200x200")
        self.root.rowconfigure(1, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.grab_set()

        top_frame = tk.Frame(self.root)
        top_frame.grid(column=1, row=1)

        tk.Label(top_frame, text="Tyllyke du vandt!").grid(column=1, row=1, columnspan=2)
        tk.Button(top_frame, text="Afslut", command=sys.exit).grid(column=1, row=2)
        tk.Button(top_frame, text="Gå til menuen", command=self.menu_return).grid(column=2, row=2)

    def menu_return(self):
        self.root.grab_release()
        self.root.destroy()
        self.destroy()
