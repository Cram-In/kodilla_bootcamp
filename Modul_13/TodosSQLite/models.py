import sqlite3


class Todos:
    def __init__(self, title, descryption):
        self.title = title
        self.descryption = descryption

    def __repr__(self):
        return "Task title {self.title} descryption: {self.descryption}"

    def add_task(task):
        with conn:
            c.execute(
                "INSERT INTO todos VALUES (:title, :description)",
                {"title": task.title, "description": task.description},
            )

    def get_task(task_id):
        c.execute("SELECT * FROM todos WHERE task_id=:task_id", {"task_id": task.id})
        return c.fetchall()

    def update_task(task, description):
        with conn:
            c.execute(
                """UPDATE todos SET description = :description
                        WHERE title = :title AND description = :description""",
                {"title": task.title, "description": task.description},
            )

    def remove_task(task):
        with conn:
            c.execute(
                "DELETE from todos WHERE title = :title AND description = :description",
                {"title": task.title, "description": task.description},
            )
