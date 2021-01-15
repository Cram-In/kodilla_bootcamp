import sqlite3


def add_task(task):
    with conn:
        c.execute(
            "INSERT INTO todo VALUES (:title, :description)", {"title": task.title, "description": task.description}
        )


def get_all(task):
    c.execute("SELECT * FROM todo WHERE title=:title", {"title": title})
    return c.fetchall()


def update_task(task, description):
    with conn:
        c.execute(
            """UPDATE todo SET description = :description
                    WHERE title = :title""",
            {"title": task.title, "description": task.description},
        )


def remove_task(task):
    with conn:
        c.execute(
            "DELETE from todo WHERE title = :title AND description = :description",
            {"title": task.description, "last": task.description},
        )