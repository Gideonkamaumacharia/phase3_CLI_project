from __init__ import conn,c

def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS tasks(
              id INTEGER PRIMARY KEY,
              title TEXT NOT NULL,
              description TEXT NOT NULL,
              deadline DATE NOT NULL,
              category TEXT NOT NULL,
              completed INTEGER DEFAULT 0
              )""")

   