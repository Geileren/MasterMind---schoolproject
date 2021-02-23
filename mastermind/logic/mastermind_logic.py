#!/usr/bin/env python3

class MastermindLogic:

    # Amount of correct guesses in colorcode
    def check_correct_guess(self, colorCode, userCode):
        self.correctGuess = 0
        for i in range(len(colorCode)):
            if colorCode[i] == userCode[i]:
                self.correctGuess += 1
        return self.correctGuess


    # Amount of correct colors in colorcode
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