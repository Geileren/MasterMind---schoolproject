#!/usr/bin/env python3

class MastermindLogic():
    def __init__(self):
        pass

    # Antallet af rigtige gæt
    def checkGuess(self, colorCode, userCode):
        self.correctGuess = 0
        for i in range(len(colorCode)):
            if colorCode[i] == userCode[i]:
                self.correctGuess += 1
        return self.correctGuess


    # Hvor mange farver er rigtige i koden
    def checkColor(self, colorCode, userCode):
        self.correctGuess = 0
        for i in range(len(colorCode)):
            if userCode[i] in colorCode:
                self.correctGuess += 1

        return self.correctGuess
