#! /usr/bin/env python

# built-in imports
from pathlib import Path

# built-in imports
import sqlite3
import mastermind

class Database:
    def __init__(self, db_path=None):
        self.path = db_path
        if self.path == None:
            self.path = f'{Path(mastermind.__file__).parent}/data/Database.db'
        self._connection = sqlite3.connect(self.path)
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
