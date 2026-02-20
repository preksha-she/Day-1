import sqlite3
import pandas as pd
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    track TEXT NOT NULL,
    stipend INTEGER
);
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS mentors (
    mentor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    mentor_name TEXT NOT NULL,
    track TEXT NOT NULL
);
""")
cursor.execute("DELETE FROM interns;")
cursor.execute("DELETE FROM mentors;")

cursor.executemany("""
INSERT INTO interns (name, track, stipend) VALUES (?, ?, ?);
""", [
    ('Aarav Sharma', 'Data Science', 15000),
    ('Priya Patel', 'Web Development', 12000),
    ('Rohan Mehta', 'Data Science', 18000),
    ('Sneha Iyer', 'UI/UX Design', 10000),
    ('Karan Verma', 'Cyber Security', 20000)
])
cursor.executemany("""
INSERT INTO mentors (mentor_name, track) VALUES (?, ?);
""", [
    ('Dr. Sharma', 'Data Science'),
    ('Ms. Kapoor', 'Web Development'),
    ('Mr. Nair', 'UI/UX Design'),
    ('Ms. Singh', 'Cyber Security')
])

conn.commit()
query = """
SELECT 
    interns.name AS intern_name,
    interns.track,
    mentors.mentor_name
FROM interns
INNER JOIN mentors
ON interns.track = mentors.track;
"""
df = pd.read_sql_query(query, conn)

print("Interns with Their Mentors:\n")
print(df)

conn.close()