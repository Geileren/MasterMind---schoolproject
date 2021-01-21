import tkinter as tk

class Header(tk.Frame):
    """The top banner of the aplication"""

    def __init__(self, main):
        super().__init__(main)
        self.main = main
        self.config(bg="#4c566a")
        self.draw_widgets()

    def draw_widgets(self):
        self.headertext = tk.Label(self, text="Mastermind", bg="#4c566a", fg="#8fbcbb",
                              font=("Roboto Medium", 48, "bold"))
        self.headertext.pack(pady=(10))
