#! /usr/bin/env python

# local imports
from mastermind.data.database import Database

class GameSettings:
    def __init__(self, db_path=None):
        self.path = db_path
        with Database(self.path) as db:
            db.execute('''CREATE TABLE IF NOT EXISTS GameSettings (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            color_code TEXT NOT NULL,
                            usable_colors TEXT NOT NULL,
                            rounds TEXT NOT NULL,
                            time TEXT NOT NULL
                            )
                           ''')