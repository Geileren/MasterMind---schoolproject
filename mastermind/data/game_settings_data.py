#! /usr/bin/env python

# local imports
from mastermind.data.utils.database import Database

class GameSettings:
    def __init__(self, db_path=None):
        with Database(db_path) as db:
            db.execute('''CREATE TABLE IF NOT EXISTS GameSettings (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            color_code TEXT NOT NULL,
                            usable_colors TEXT NOT NULL,
                            rounds TEXT NOT NULL,
                            time TEXT NOT NULL
                            )
                           ''')

    def add(self, name, color_code, usable_colors, rounds, time):
        pass

    def remove(self, id):
        pass

    def get_all(self, id):
        pass