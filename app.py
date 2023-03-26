"""SQLite"""
import json
from pathlib import Path
import sqlite3

movies = json.loads(Path("movies.json").read_text())

with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)
    for data in cursor:
        print({"id": data[0], "title": data[1], "year": data[2]})
    conn.commit()
