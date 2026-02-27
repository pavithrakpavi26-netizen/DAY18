import sqlite3
import pandas as pd

# 1️ Connect to Database
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

# 2️ Create interns table
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    track TEXT NOT NULL,
    stipend INTEGER
)
""")

# Clear old data (optional for re-running notebook)
cursor.execute("DELETE FROM interns")

# Insert sample interns
intern_data = [
    (1, "Aisha", "Data Science", 15000),
    (2, "Rahul", "Web Dev", 12000),
    (3, "Meena", "Data Science", 18000),
    (4, "Arjun", "Web Dev", 10000),
    (5, "Priya", "UI/UX", 14000)
]

cursor.executemany("INSERT INTO interns VALUES (?, ?, ?, ?)", intern_data)

# 3️ Create mentors table
cursor.execute("""
CREATE TABLE IF NOT EXISTS mentors (
    mentor_id INTEGER PRIMARY KEY,
    mentor_name TEXT NOT NULL,
    track TEXT NOT NULL
)
""")

# Clear old data (optional)
cursor.execute("DELETE FROM mentors")

# Insert sample mentors
mentor_data = [
    (1, "Dr. Sharma", "Data Science"),
    (2, "Ms. Kapoor", "Web Dev"),
    (3, "Mr. Iyer", "UI/UX")
]

cursor.executemany("INSERT INTO mentors VALUES (?, ?, ?)", mentor_data)

# Save changes
conn.commit()

# 4️ INNER JOIN Query
query = """
SELECT interns.name,
       interns.track,
       mentors.mentor_name
FROM interns
INNER JOIN mentors
ON interns.track = mentors.track;
"""

# 5️ Load into Pandas DataFrame
df = pd.read_sql_query(query, conn)

print("Joined Data:")
print(df)

# Close connection
conn.close()

