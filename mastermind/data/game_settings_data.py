#! /usr/bin/env python

# local imports
from mastermind.data.database import Database


class GameSettings:
    def __init__(self, path=None):
        with Database(path) as db:
            db.execute('''CREATE TABLE IF NOT EXISTS GameSettings (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            color_code TEXT NOT NULL,
                            usable_colors INTEGER NOT NULL,
                            rounds INTEGER NOT NULL,
                            rounds_played INTEGER NOT NULL,
                            time TEXT NOT NULL
                            )
                           ''')
    
    def add(self, name, color_code_raw, usable_colors, rounds, rounds_played, time):
        color_code = '_'.join(color_code_raw)
        with Database() as db:
            db.execute('INSERT INTO GameSettings (name, color_code, usable_colors, rounds, rounds_played, time) VALUES (?,?,?,?,?,?)', (name, color_code, usable_colors, rounds, rounds_played, time))

    def get(self, id):
        with Database() as db:
            return db.query_one('SELECT * FROM GameSettings WHERE id=?', (id,))[0]

    def get_all(self):
        with Database() as db:
            return db.query_all('SELECT * FROM GameSettings')

    def remove(self, id):
        with Database() as db:
            db.execute('DELETE FROM GameSettings WHERE id=?', (id,))