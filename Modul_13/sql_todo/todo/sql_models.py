import sqlite3


conn = sqlite3.connect("todo.db")

c = conn.cursor()

c.execute(
    """ CREATE TABLE todo (
    id integer PRIMARY KEY,
    title text NOT NULL,
    description text NOT NULL
)"""
)

conn.close()