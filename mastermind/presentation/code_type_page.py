#!/usr/bin/env python

# built-in imports
import tkinter as tk

# local imports
from mastermind.presentation.game_page import GamePage
from mastermind.presentation.components.but_types import GameButton, ColorButton
from mastermind.data.mastermind_data import color_list
from mastermind.data.mastermind_data import ColorCode

class CodeInputPage(tk.Frame):
    def __init__(self, multi_color, main=None):
        super().__init__(main)
        self.main = main
        self.config(bg="#2E3440")
        self.main.geometry('600x500')
        self.draw_widget()
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        self.color_code = ColorCode()
        
        # used for color palette and checking for multi color
        self.multi_color = multi_color
        self.colormode = "clear"
        self.colormode_status = False


    def draw_widget(self):

        # Overall frame
        self.frame = tk.Frame(self, bg="#2E3440")
        self.frame.grid(column=1, row=1)

        # palette and code input 
        self.color_frame =tk.Frame(self.frame)
        self.color_frame.grid(column=1, row=0, columnspan=5, pady=25)

        tk.Label(self.frame, text="Vælg en farve ovenfor og placer den i koden herunder", bg="#2E3440", fg="#8fbcbb").grid(column=1, row=1, columnspan=5)

        self.game_frame = tk.Frame(self.frame)
        self.game_frame.grid(column=1, row=2, columnspan=5, pady=5)

        self.buttons = [GameButton(self.game_frame, x, 1, self) for x in range(4)]
        for i in self.buttons:
            i.button.config(state="normal")
        
        self.color_buttons = [ColorButton(self.color_frame, i // 4, i % 4, j, self) for i, j in enumerate(color_list)]
        
        # start and back buttons
        self.start_but = tk.Button(self.frame, text="Start spil", command=self.start, bg="#434C5E", fg="#8fbcbb")
        self.start_but.grid(column=4, row=2, sticky="E")

        self.back_but = tk.Button(self.frame, text="Tilbage til startmenuen", command=self.destroy, bg="#434C5E", fg="#8fbcbb")
        self.back_but.grid(column=3, row=2, sticky="E", padx=(400,0))

    # saves the code in the input buttons
    def save_code(self):
        return [i.color for i in self.buttons]
    
    # should be moved to logic-layer in next update 
    def multi_check(self, lst1):
        # checks if a colors is used more than once
        for i in lst1:
            lst2 = lst1
            lst2.remove(i)
            for j in lst2:
                if i == j:
                    return False
        return True

    # continues to next frame
    def start(self):
        code = self.save_code()
        
        # checks if there are any messing colors
        if "" in code:
            self.error1()

        elif self.multi_color == False:
            
            if self.multi_check(code) == True:
                # saves code to data
                self.color_code.make(self.save_code())
                
                self.destroy()
                GamePage(self.color_code, self.main).grid(column=1, row=1, sticky="NEWS")

            else:
                # if a color is used multiple times
                self.error2()
                pass
        else:
            # any color combination goes
            self.color_code.make(code)
            
            self.destroy()
            GamePage(self.color_code, self.main).grid(column=1, row=1, sticky="NEWS")

    def error1(self):
        # error pup-up 1
        self.root1 = tk.Toplevel()
        tk.Label(self.root1, text="Nogle af kodefelterne er ikke udfyldt, udfyld disse og prøv igen").grid(column=1, row=1)
        tk.Button(self.root1, text="OK", command=self.close1).grid(column=1, row=2)
        self.root1.grab_set()

    def error2(self):
        # error pup-up 2
        self.root2 = tk.Toplevel()
        tk.Label(self.root2, text="Du har indtastet den samme farve mere end én gang. Det er ikke tilladt med de nuværende regler. \n Ændre koden og prøv igen").grid(column=1, row=1)
        tk.Button(self.root2, text="OK", command=self.close2).grid(column=1, row=2)
        self.root2.grab_set()

    def close1(self):
        # closes error pup-up 1
        self.root1.grab_release()
        self.root1.destroy()

    def close2(self):
        # closes error pup-up 2
        self.root2.grab_release()
        self.root2.destroy()

    def clear_color_mode(self):
        # only one palette color can be used at a time
        if self.colormode_status == True:
            self.colormode = "clear"
            self.colormode_status = False
            for i in self.color_buttons:
                i.button.config(relief="raised")