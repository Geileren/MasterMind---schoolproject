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
                            usable_colors TEXT NOT NULL,
                            rounds TEXT NOT NULL,
                            time TEXT NOT NULL
                            )
                           ''')
    
    def add(self, name, color_code, usable_colors, rounds, time):
        with Database() as db:
            db.execute('INSERT INTO GameSettings (name, color_code, usable_colors, rounds, time) VALUES (?,?,?,?,?)', (name, color_code, usable_colors, rounds, time))


if __name__ == '__main__':
    GameSettings().add('test', "('red', 'blue')", "('red', 'blue', 'green')", '10', '2')