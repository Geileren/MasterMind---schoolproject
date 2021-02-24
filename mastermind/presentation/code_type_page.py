#!/usr/bin/env python

# built-in imports
import tkinter as tk

# local imports
from mastermind.presentation.game_page import GamePage
from mastermind.presentation.components.but_types import GameButton, ColorButton
from mastermind.data.mastermind_data import color_list

class CodeInputPage(tk.Frame):
    def __init__(self, multi_color, main=None):
        super().__init__(main)
        self.main = main
        self.config(bg="#4c566a")
        self.draw_widget()
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        
        self.multi_color = multi_color

        self.colormode = "clear"
        self.colormode_status = False


    def draw_widget(self):

        # Overall frame
        self.frame = tk.Frame(self, bg="#4c566a")
        self.frame.grid(column=1, row=1)

        self.game_frame = tk.Frame(self.frame)
        self.game_frame.grid(column=1, row=1)

        self.color_frame =tk.Frame(self.frame)
        self.color_frame.grid(column=2, row=1)

        self.buttons = [GameButton(self.game_frame, x, 1, self) for x in range(4)]
        for i in self.buttons:
            i.button.config(state="normal")
        
        self.color_buttons = [ColorButton(self.color_frame, i // 4, i % 4, j, self) for i, j in enumerate(color_list)]
        

        self.start_but = tk.Button(self.frame, text="Din Mor Thien", command=self.start)
        self.start_but.grid(column=3, row=2)

    def save_code(self):
        return [i.color for i in self.buttons]
    
    def multi_check(self, lst):
        for i in lst:
            lst2 = lst
            lst2.remove(i)
            for j in lst2:
                if i == j:
                    return False
        return True


    def start(self):
        code = self.save_code()
        if "" in code:
            self.error1()
        elif self.multi_color == False:
            if self.multi_check(code) == True:
                #mere shit
                GamePage(self.main).grid(column=1, row=1, sticky="NEWS")
            else:
                self.error2()
                pass
        else:
            GamePage(self.main).grid(column=1, row=1, sticky="NEWS")

    def error1(self):
        self.root1 = tk.Toplevel()
        tk.Label(self.root1, text="Nogle af kodefelterne er ikke udfyldt, udfyld disse og prøv igen").grid(column=1, row=1)
        tk.Button(self.root1, text="OK", command=self.close1).grid(column=1, row=2)
        self.root1.grab_set()

    def error2(self):
        self.root2 = tk.Toplevel()
        tk.Label(self.root2, text="Du har indtastet den samme farve mere end én gang. Det er ikke tilladt med de nuværende regler. \n Ændre koden og prøv igen").grid(column=1, row=1)
        tk.Button(self.root2, text="OK", command=self.close2).grid(column=1, row=2)
        self.root2.grab_set()

    def close1(self):
        self.root1.grab_release()
        self.root1.destroy()

    def close2(self):
        self.root2.grab_release()
        self.root2.destroy()

    def clear_color_mode(self):
        if self.colormode_status == True:
            self.colormode = "clear"
            self.colormode_status = False
            for i in self.color_buttons:
                i.button.config(relief="raised")