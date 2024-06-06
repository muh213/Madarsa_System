import sqlite3

# Connect to the database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Insert statement and sample data
insert_query = "INSERT INTO students (std_fname, std_lname, iqama, std_fno, std_sno) VALUES (?, ?, ?, ?, ?)"
data_list = [
    ("Master", "Idiot", "0123456789", "+17323096811", "999"),
    ("Hayyan", "Abdullah", "2123456789", "+966593790525", "998"),
    ("Muhammad", "Alam", "2987654321", "0593348477", "911"),
]

# Insert data into the table
cursor.executemany(insert_query, data_list)

# Commit changes and close the connection
conn.commit()
print("Data inserted successfully!")
conn.close()
