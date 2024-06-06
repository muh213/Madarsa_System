import sqlite3

# Connect to the database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Update statement and sample data
update_query = "UPDATE students SET std_fname = ?, std_lname = ?, std_fno = ?, std_sno = ? WHERE iqama = ?"
data_list = [
    ("John", "Doe", "17323096811", "0593790525", "2554545455454"),
    ("Jane", "Smith", "0593348477", "059485231", "25495465465465"),
]

# Update data in the table
for data in data_list:
    cursor.execute(update_query, data)

# Commit changes and close the connection
conn.commit()
print("Data updated successfully!")
conn.close()
