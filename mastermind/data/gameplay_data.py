#! /usr/bin/env python

# local imports
from mastermind.data.database import Database

class Gameplay:
    def __init__(self, path=None):
        with Database(path) as db:
            db.execute('''CREATE TABLE IF NOT EXISTS Gameplay (
                            round_id INTEGER PRIMARY KEY NOT NULL,
                            guess TEXT NOT NULL,
                            game_settings_id INTEGER NOT NULL,
                            FOREING KEY(game_settings_id) REFERENCES GameSettings(id) ON DELETE CASCADE
                            )
                           ''')

    def add(self, round_id, guess, game_settings_id):
        with Database() as db:
            db.execute('INSERT INTO Gameplay(round_id, guess, game_settings_id) VALUES (?,?,?)', (round_id, guess, game_settings_id))

    def get_all(self, game_settings_id):
        with Database() as db:
            db.query_all('SELECT * FROM Gameplay WHERE game_settings_id=?', (game_settings_id,))