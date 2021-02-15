#!/usr/bin/env python3
import unittest
from mastermind.logic.logic import MastermindLogic

class logic_unittest(unittest.TestCase):
    def test_checkGuess(self):
        self.colorCode = [1,2,3,4]
        self.userCode = [3,4,5,6]

        self.assertEqual(MastermindLogic().checkGuess(self.colorCode, self.userCode), 0)

        self.userCode = 
        self.asserEqual(MastermindLogic().checkGuess(self.colorCode, self.usercode), 4)

    def test_checkColor(self):
        pass

if __name__ == "__main__":
    unittest.main()
