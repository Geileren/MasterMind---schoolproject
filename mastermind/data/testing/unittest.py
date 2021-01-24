#!/usr/bin/env python

# local imports
from mastermind.data.utils.database import Database
from mastermind.data.game_settings_data import GameSettings

# built-in imports
import unittest

class TestGameSettingsData(unittest.TestCase):
    """Test for the game_settigns_data.py"""
    def setUp(self):
        self.game_settings = GameSettings(':memory:')

    def test_add(self):
        pass

    def test_remove(self):
        pass

    def test_get_all(self):
        pass