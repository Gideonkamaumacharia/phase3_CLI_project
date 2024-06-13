from __init__ import conn,c
import datetime

class TasksDb:
    def __init__(self):
        self.conn = conn
        self.c = c
    
    def add_task(self,title,description, deadline,category,completed=0):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.category = category
        self.completed = completed
    
        c.execute("""INSERT INTO tasks(title,description,deadline,category,completed) VALUES (?,?,?,?,?)""",(self.title, self.description, self.deadline, self.category, self.completed))

        conn.commit()
        print("Task added successfully.")
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Title cannot be empty.")
        self._title = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if not value:
            raise ValueError("Description cannot be empty.")
        self._description = value

    @property
    def deadline(self):
        return self._deadline

    @deadline.setter
    def deadline(self, value):
        try:
            datetime.datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Deadline should be in YYYY-MM-DD format.")
        self._deadline = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not value:
            raise ValueError("Category cannot be empty.")
        self._category = value

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
    
    def get_task_by_id(self, task_id):
        c.execute('''SELECT * FROM tasks WHERE id = ?''', (task_id,))
        task = c.fetchone()
        if task:
            return task
        else:
            print("Task not found.")
            return None

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
    
    def get_category_by_id(self, category_id):
        c.execute('''SELECT * FROM categories WHERE id = ?''', (category_id,))
        category = c.fetchone()
        if category:
            return category
        else:
            print("Category not found.")
            return None

    
    def delete_tasks(self,task_id):
        c.execute('''DELETE FROM tasks WHERE id =?''',(task_id,))
        conn.commit()
        print("Task deleted successfully.")

    def delete_category(self,category_id):
        c.execute('''DELETE FROM categories WHERE id = ?''',(category_id,))
        conn.commit()
        print("Category deleted")

    def close(self):
        conn.close()