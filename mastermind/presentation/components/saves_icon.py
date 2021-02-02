import tkinter as tk

class Save_icon:

    def __init__(self, root, nr, column, row):
        self.root = root
        self.nr = nr
        self.column = column
        self.row = row
        self.status = False
        self.status_text = "Ingen gemt spil"

        self.check_status()
        self.draw_widgets()

    def check_status(self):
        pass


    def draw_widgets(self):
        self.frame = tk.Frame(self.root, bg="#2E3440", highlightbackground="black", highlightthickness=0.5)
        self.frame.grid(column=self.column, row=self.row)

        self.status_label = tk.Label(self.frame, text=f"Status: {self.status_text}", bg="#2E3440", fg="#8fbcbb")
        self.status_label.grid(column=1, row=1, padx=5, pady=(3,0))

        self.load_button = tk.Button(self.frame, text="Hent Spil", bg="#434C5E", fg="#8fbcbb", command=self.load_game)
        self.load_button.grid(column=1, row=2, pady=(0,3))

    def load_game(self):
        pass
