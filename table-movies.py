import sqlite3
import cs50
import csv
import sys
import os

# Check command line arguments
if len(sys.argv) != 2:
    print("Usage: python3 tables-movies.py data/year.csv")
    sys.exit(1)

start_year = sys.argv[1].strip('data/').strip('.csv')

open(f"table-movies-{start_year}.db", "w").close()
db = cs50.SQL(f"sqlite:///table-movies-{start_year}.db")

db.execute(
    "CREATE TABLE movies (rank NUMERIC, title TEXT, worldwide NUMERIC, domestic NUMERIC)")

with open(sys.argv[1], 'r') as file:
    reader = csv.DictReader(file, delimiter=",")

    for row in reader:

        rank = row['Rank']
        title = row['Release Group']
        worldwide = row['Worldwide']
        domestic = row['Domestic']

        db.execute("INSERT INTO movies (rank, title, worldwide, domestic) VALUES (?,?,?,?)",
                   rank, title, worldwide, domestic)
