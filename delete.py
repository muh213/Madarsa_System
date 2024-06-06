import sqlite3

# Connect to the database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Delete statement and sample data
delete_query = "DELETE FROM students WHERE iqama = ?"
data_list = [
    ("0123456789",),
    ("2123456789",),
    ("2987654321",),
]

# Delete data from the table
for iqama in data_list:
    cursor.execute(delete_query, iqama)

# Commit changes and close the connection
conn.commit()
print("Data deleted successfully!")
conn.close()
