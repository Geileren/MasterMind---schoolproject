#! /usr/bin/env python

# built-in imports
from pathlib import Path
import sqlite3

# local imports
import mastermind

class Database:
    def __init__(self, db_path=None):
        if db_path == None:
            self.path = f'{Path(mastermind.__file__).parent}/data/Database.db'
        else:
            self.path = db_path
            
        self._connection = sqlite3.connect(self.path)
        #self._connection.execute('PRAGMA foreign_keys = 1')
        self._cursor = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    @property
    def connection(self):
        return self._connection

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()
