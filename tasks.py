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

    def view_tasks(self):
        c.execute('''SELECT * FROM tasks WHERE completed = 0 ORDER BY deadline ASC''')
        tasks = c.fetchall()
        if not tasks:
            print("No pending tasks.")
        else:
            for task in tasks:
                print(task)

    def add_category(self,name):
        c.execute('''INSERT INTO categories (name) VALUES (?)''', (name,))
        conn.commit()
        print("Category added successfully.")

    def view_categories(self):
        c.execute('''SELECT * FROM categories''')
        categories = c.fetchall()
        if not categories:
            print("No categories found.")
        else:
            for category in categories:
                print(category)
    
    def close(self):
        conn.close()
    
def main():
    
    db = TasksDb()
    
    while True:
        print("\nTask Manager CLI\n")
        print("1.Add Task")
        print("2.Mark Task As Complete")
        print("3. View Tasks")
        print("4. Add Category")
        print("5. View Categories")
        print("6. Exit")


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

        elif choice == '3':
            db.view_tasks()

        elif choice == '4':
            name = input("Enter category name: ")
            db.add_category(name)

        elif choice == '5':
            db.view_categories() 

        elif choice == '6':
            db.close()
            break

        else:
            print("Invalid choice. Please try again.")

            


if __name__== "__main__":
    main()
    
   