#! /usr/bin/env python

# local imports
from mastermind.data.database import Database

class Gameplay:
    def __init__(self, db_path=None):
        with Database(db_path) as db:
            db.execute('''CREATE TABLE IF NOT EXISTS Gameplay (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            round INTEGER NOT NULL,
                            guess TEXT NOT NULL,
                            game_settings_id INTEGER NOT NULL,
                            )
                           ''')