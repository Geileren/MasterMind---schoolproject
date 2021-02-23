#!/usr/bin/env python3

# Built-in imports
from random import randint, shuffle

class MastermindLogic:
    def check_correct_guess(self, colorCode, userCode):
        self.correctGuess = 0
        for i in range(len(colorCode)):
            if colorCode[i] == userCode[i]:
                self.correctGuess += 1
        return self.correctGuess

    def check_correct_color(self, colorCode, userCode):
        self.correctGuess = 0
        for i in range(len(colorCode)):
            if userCode[i] in colorCode:
                self.correctGuess += 1
        return self.correctGuess

    def check_win(self, colorCode, userCode):
        if userCode == colorCode:
            return True
        return False

    def check_gamestate(self, colorCode, userCode):
        self.correct_guesses = self.check_correct_guess(colorCode, userCode)
        self.correct_colors = self.check_correct_color(colorCode, userCode) - self.correct_guesses
        return (self.check_win(colorCode, userCode), self.correct_guesses, self.correct_colors)

    def generate_code(self, colors):
        return [colors[randint(0, len(colors)-1)] for _ in range(4)]

    def generate_unique_code(self, colors):
        if len(colors) >= 4:
            shuffle(colors)
            return colors[:4]
