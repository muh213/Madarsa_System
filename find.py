import sqlite3

# Connect to the database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()
# Select all statement
select_query = "SELECT * FROM students"

# Execute the query
cursor.execute(select_query)

# Fetch all results
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the connection
conn.close()
