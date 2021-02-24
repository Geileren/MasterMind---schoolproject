#! /usr/bin/env python

# Colors used ingame for guessing
color_list = ["#BF616A", "#D08770", "#EBCB8B", "#A3BE8C", "#B48EAD", "#566DDB", "#adb8eb", "#99c1de"]

class ColorCode:
    def __init__(self):
        self.manual_code = []

    def make(self, colors):
        self.manual_code = colors

    def get(self):
        if self.manual_code != []:
            return self.manual_code