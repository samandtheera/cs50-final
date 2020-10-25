import sqlite3
import cs50
import csv
import sys

# Check command line arguments
if len(sys.argv) < 2:
    print("Usage: python3 movie-roster.py YEAR RANK")
    sys.exit(1)

year = sys.argv[1]
rank = sys.argv[2]

db = cs50.SQL(f"sqlite:///table-movies-{year}.db")

table = db.execute(
    "SELECT title, worldwide, domestic FROM movies WHERE rank = ?", rank)
for row in table:
    title = row['title']
    worldwide = row['worldwide']
    domestic = row['domestic']
print(
    f"The box office rank {rank} from {year} is {title}. It has made {worldwide} overall, of which {domestic} was made in the US.")
