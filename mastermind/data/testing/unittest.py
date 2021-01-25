#!/usr/bin/env python

# local imports
from mastermind.data.utils.database import Database
from mastermind.data.game_settings_data import GameSettings

# built-in imports
import unittest
#from mastermind.data.game_settings_data import GameSettings

class TestGameSettingsData(unittest.TestCase):
    """Test for the game_settigns_data.py"""
    def setUp(self):
        self.game_settings = GameSettings(':memory:')

    def test_add(self):
        self.assertEqual(GameSettings.add("joemama", ["#BF616A", "#D08770", "#EBCB8B", "#A3BE8C", "#88C0D0"], 4, 10, "00:00"), GameSettings.get_all(1))

    def test_remove(self):
        pass

    def test_get_all(self):
        pass