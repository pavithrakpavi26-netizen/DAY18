
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

# Clear old data (so notebook can re-run safely)
cursor.execute("DELETE FROM interns")

# Insert sample data
intern_data = [
    (1, "Aisha", "Data Science", 15000),
    (2, "Rahul", "Web Dev", 12000),
    (3, "Meena", "Data Science", 18000),
    (4, "Arjun", "Web Dev", 10000),
    (5, "Priya", "UI/UX", 14000)
]

cursor.executemany("INSERT INTO interns VALUES (?, ?, ?, ?)", intern_data)
conn.commit()


# 3️ FILTER QUERY
# Find Data Science interns with stipend > 5000
query_filter = """
SELECT *
FROM interns
WHERE track = 'Data Science'
AND stipend > 5000;
"""

df_filter = pd.read_sql_query(query_filter, conn)

print("Filtered Data (Data Science & stipend > 5000):")
print(df_filter)
print("\n")


# 4️ AGGREGATE QUERY
# Average stipend per track
query_avg = """
SELECT track,
       AVG(stipend) AS avg_stipend
FROM interns
GROUP BY track;
"""

df_avg = pd.read_sql_query(query_avg, conn)

print("Average Stipend per Track:")
print(df_avg)
print("\n")


# 5️ COUNT QUERY
# Count interns per track
query_count = """
SELECT track,
       COUNT(*) AS total_interns
FROM interns
GROUP BY track;
"""

df_count = pd.read_sql_query(query_count, conn)

print("Total Interns per Track:")
print(df_count)


# 6️ Close Connection
conn.close()

