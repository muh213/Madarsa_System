import cv2
import numpy as np
from pyzbar.pyzbar import decode
import sqlite3
import webbrowser

check = "0000000"  # Initialize video capture
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(cv2.CAP_PROP_EXPOSURE, -1)

# Connect to the database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Fetch iqama values from the database and convert to a list of integers
cursor.execute("SELECT iqama FROM students")
results_list = [row[0] for row in cursor.fetchall()]
last_barcode = ""

while True:
    success, img = cap.read()
    if not success:
        break

    for barcode in decode(img):
        myData = barcode.data.decode("utf-8")
        print(myData)
        if int(myData) in results_list and myData != last_barcode:
            select_query = "SELECT std_fno FROM students WHERE iqama = ?"
            cursor.execute(select_query, (myData,))
            number = cursor.fetchall()
            for row in number:
                phoneno = int(row[0])
                print(row)
            print(phoneno)
            last_barcode = myData
            myOutput = "Authorized"
            myColor = (0, 255, 0)
            html_file_path = "hello.html"
            webbrowser.open(html_file_path)

        else:
            myOutput = "Un-Authorized"
            myColor = (0, 0, 255)

        pts = np.array([barcode.polygon], np.int32).reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, myColor, 5)
        pts2 = barcode.rect
        cv2.putText(
            img, myOutput, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, myColor, 2
        )

    cv2.imshow("Result", img)
    if cv2.waitKey(1) == 27:  # Exit if 'Esc' key is pressed
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
conn.close()
