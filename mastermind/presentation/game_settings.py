#!/usr/bin/env python3

# built-in imports
import tkinter as tk

class GameSettings(tk.Frame):
    """A frame for the game settings"""

    def __init__(self, main):
        super().__init__(main)
        self.main = main
        self.main.title('Spil indstillinger')
    
    def draw_widgets(self):
        checkVar1 = IntVar()
        checkVar2 = IntVar()

        # Labels
        self.galaxyBrain = tk.Label(self, text = "Galaxy brain mode")
        self.genCode = tk.Label(self, text = "Generer en kode")
        self.sameColor = tk.Label(self, text = "Den samme farve kan optræde flere gange")

        # Checkboxes
        self.galaxyBrainCheck = tk.Checkbutton(self, variable = checkVar1)
        self.sameColor = tk.Checkbutton(self, variable = checkVar2)

        # Radiobuttons
        self.galaxyBrainBox = tk.Radiobutton(self)


        # Frame




def main():
    root = tk()
    root.mainloop()


if __name__ == "__main__":
    main()
