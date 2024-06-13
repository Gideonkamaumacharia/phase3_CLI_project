from taskDb import TasksDb
from __init__ import conn,c


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
  

create_table()


    
def main():
    
    db = TasksDb()
    
    while True:
        print("\nTask Manager CLI\n")
        print("1. Add Task")
        print("2. Mark Task As Complete")
        print("3. View Tasks")
        print("4. Get Tasks by ID")
        print("5. Add category")
        print("6. View Categories")
        print("7. Delete Task")
        print("8. Delete Category")
        print("9. Exit")
       


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
            task_id = input("Enter task ID to view: ")
            task = db.get_task_by_id(task_id)
            if task:
                print("Task Details:")
                print(f"ID: {task[0]}")
                print(f"Title: {task[1]}")
                print(f"Description: {task[2]}")
                print(f"Deadline: {task[3]}")
                print(f"Category: {task[4]}")
                print(f"Completed: {'Yes' if task[5] else 'No'}")

        elif choice == '5':
            name = input("Enter category name: ")
            db.add_category(name)

        elif choice == '6':
            db.view_categories() 
        
        elif choice == '7':
            task_id = input("Enter task ID to delete: ")
            db.delete_tasks(task_id)

        elif choice == '8':
            category_id = input("Enter task category ID: " )
            db.delete_category(category_id)

        elif choice == '9':
            db.close()
            break
        
       

        else:
            print("Invalid choice. Please try again.")

            


if __name__== "__main__":
    main()
    
   