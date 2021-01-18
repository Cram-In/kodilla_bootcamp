import sqlite3


conn = sqlite3.connect("todos.db")
c = conn.cursor()

conn.execute(
    """CREATE TABLE todo (
            id INTEGER PRIMARY KEY,
            title char(50) NOT NULL,
            description char(200) NOT NULL
            )"""
)
