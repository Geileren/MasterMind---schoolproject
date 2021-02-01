#!/usr/bin/env python3

import unittest
from mastermind.data.game_settings_data import GameSettings

class data_unittest(unittest.TestCase):
    def setUp(self):
        self.game_settings = GameSettings(':memory:')

    def test_create(self):
        self.assertEqual(GameSettings.add("joemama", ["#BF616A", "#D08770", "#EBCB8B", "#A3BE8C", "#88C0D0"], 4, 10, "00:00"), GameSettings().get_all(1))

    def test_read(self):
        self.assertEqual(GameSettings.add("joefather", ["#BF616A", "#D08770", "#EBCB8B", "#A3BE8C", "#88C0D0"], 4, 10, "00:00"), GameSettings().get_all(1))

    def test_update(self):
        GameSettings.add("joejoe", ["#BF616A", "#D08770", "#EBCB8B", "#A3BE8C", "#88C0D0"], 4, 10, "00:00")
        GameSettings.delete("joejoe")
        self.assertEqual(GameSettings.add("joefather", ["#BF616A", "#D08770", "#EBCB8B", "#A3BE8C", "#88C0D0"], 4, 10, "00:00"), GameSettings().get_all(1))

    def test_delete(self):
        GameSettings.add("eoj", ["#BF616A", "#D08770", "#EBCB8B", "#A3BE8C", "#88C0D0"], 4, 10, "00:00")
        GameSettings.delete("eoj")
        self.assertEqual((), GameSettings().get_all(1))

    def tearDown(self):
        pass



