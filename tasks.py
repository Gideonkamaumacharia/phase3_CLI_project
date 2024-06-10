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
    #conn.close()

create_table()

class TasksDb:
    def __init__(self):
        self.conn = conn
        self.c = c
    
    def add_task(self,title,description, deadline,category):
        self.c.execute("""INSERT INTO tasks VALUES (?,?,?,?)""",(title,description,deadline,category))

        conn.commit()
        print("Task added successfully.")

    
def main():
    
    db = TasksDb()
    
    while True:
        print("\nTask Manager CLI\n")
        print("1.Add Task")

        choice  = input("\nEnter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            deadline = input("Enter the task deadline (YYYY-MM-DD): ")
            category = input("Enter the task category: ")
            db.add_task(title,description, deadline,category)

            


if __name__== "__main__":
    main()
    
   