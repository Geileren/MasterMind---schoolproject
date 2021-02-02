#! /usr/bin/env python

from pathlib import Path
import mastermind

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
                            usable_colors INTEGER NOT NULL,
                            rounds INTEGER NOT NULL,
                            time TEXT NOT NULL
                            )
                           ''')
    
    def add(self, name, color_code, usable_colors, rounds, time):
        with Database() as db:
            db.execute('INSERT INTO GameSettings (name, color_code, usable_colors, rounds, time) VALUES (?,?,?,?,?)', (name, color_code, usable_colors, rounds, time))

    def get(self, id):
        pass

    def remove(self, id):
        pass
