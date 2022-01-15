import psycopg2
from psycopg2 import Error
import face_recognition
import cv2

conn = psycopg2.connect(user="myujhxdwmlfrvs",
password="1e02f632d3a9a1d2693c600698c6c57e837385c7bae86d8539fc31a42cdfb3ff",
host="ec2-3-231-253-230.compute-1.amazonaws.com",
port="5432",
database="d6sq4eottr7e0i")

# Setting auto commit false

conn.autocommit = True

# Creating a cursor object using the cursor() method

cursor = conn.cursor()

# Retrieving data

cursor.execute('''SELECT image from student_infor''')

#Fetching 1st row from the table

result = cursor.fetchone();
print(result)

#Fetching 1st row from the table


#Commit your changes in the database

conn.commit()

def is_match_person(source,unknown):
    known_image = face_recognition.load_image_file(source)

    unknown_image = face_recognition.load_image_file(unknown)

    if face_recognition.face_encodings(known_image) and face_recognition.face_encodings(unknown_image):
        biden_encoding = face_recognition.face_encodings(known_image)[0]
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

        results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
        return results
    else:
        return False

for facePath in result:
    if is_match_person(facePath, "./img/obama.jpeg")[0]:
        cursor.execute("SELECT name from student_infor where image='{}'".format(facePath))
        print('WELCOME ' + cursor.fetchone()[0])
        break;
    print(False)

#Closing the connection

conn.close()
