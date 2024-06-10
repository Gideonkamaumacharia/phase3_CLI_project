from __init__ import conn,c
import sqlite3

def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS tasks(
              id INTEGER PRIMARY KEY AUTOINCREMENT
              ,
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
    
    def add_task(self,title,description, deadline,category,completed=0):
        self.c.execute("""INSERT INTO tasks(title,description,deadline,category,completed) VALUES (?,?,?,?,?)""",(title,description,deadline,category,completed))

        conn.commit()
        print("Task added successfully.")

    def mark_task_completed(self,task_id):
        c.execute('''UPDATE tasks SET completed = 1 WHERE id = ?''', (task_id,))
        conn.commit()
        print("Task marked as completed.")

    
def main():
    
    db = TasksDb()
    
    while True:
        print("\nTask Manager CLI\n")
        print("1.Add Task")
        print("2.Mark Task As Complete")

        choice  = input("\nEnter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            deadline = input("Enter the task deadline (YYYY-MM-DD): ")
            category = input("Enter the task category: ")
            db.add_task(title,description, deadline,category)
        
        elif choice == '2':
            task_id = input("Enter task ID to mark as completed: ")
            db.mark_task_completed(task_id)

            


if __name__== "__main__":
    main()
    
   