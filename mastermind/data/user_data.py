#! /usr/bin/env python

# local imports
from mastermind.data.database import Database

class User:
    def __init__(self):
        with Database() as db:
            db.execute('''CREATE TABLE IF NOT EXISTS user (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            password TEXT NOT NULL
                            )
                           ''')
    
    def add(self, name, password):
        with Database() as db:
            db.execute('''test''')