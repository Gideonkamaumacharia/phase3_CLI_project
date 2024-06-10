from __init__ import conn,c
import sqlite3

def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS tasks(
              id INTEGER PRIMARY KEY,
              title TEXT NOT NULL,
              description TEXT NOT NULL,
              deadline DATE NOT NULL,
              category TEXT NOT NULL,
              completed INTEGER DEFAULT 0
              )""")
    c.execute("""CREATE TABLE IF NOT EXISTS categories(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL
              )""")
    conn.commit()
    conn.close()

create_table()

class Tasks:
    def __init__(self):
        self.conn = sqlite3.connect("tasks_manager.db")
        self.c = self.conn.cursor()

    
        




   