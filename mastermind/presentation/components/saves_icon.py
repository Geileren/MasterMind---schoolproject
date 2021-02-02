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
        self.frame = tk.Frame(self.root)
        self.frame.grid(column=self.column, row=self.row)

        self.status_label = tk.Label(self.frame, text=f"Status: {self.status_text}")
        self.status_label.grid(column=1, row=1)

        self.load_button = tk.Button(self.frame, text="Hent Spil", command=self.load_game)
        self.load_button.grid(column=1, row=2)

    def load_game(self):
        pass
