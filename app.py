"""SQLite"""
import json
from pathlib import Path
import sqlite3

movies = json.loads(Path("movies.json").read_text())
print(movies)

sqlite3.connect("db.sqlite3")
