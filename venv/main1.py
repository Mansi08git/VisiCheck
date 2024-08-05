# importing libraries
import csv
import cv2
import os
import pickle
import numpy as np
import face_recognition
import cvzone
from datetime import datetime
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("venv\\serviceAccountKey.json")
firebase_admin.initialize_app(
    cred, {"databaseURL": "https://visicheck-12e19-default-rtdb.firebaseio.com/"}
)


# set to store the id of detected face
detected_faces = set()
# initializing webcam
cap = cv2.VideoCapture(0)


# Load the encoding file
file = open("Encoding.p", "rb")
encode_list = pickle.load(file)
# jaise encode list and stu name ko ek sath kiya tha
# just like that we have to separate it again
file.close()
encodeList, stu_name = encode_list
print(stu_name)
counter = 0
names = ""


attendance_marked = False
while True:
    suc, img = cap.read()
    # resize image to smale so that less power consumption occurs
    imgs = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)

    # take img and make its encoding and compare with the encodings of known faces
    faceframe = face_recognition.face_locations(imgs)
    encodeframe = face_recognition.face_encodings(imgs, faceframe)

    # compare
    for encode, face in zip(encodeframe, faceframe):
        # comparing encode image with encode list
        matches = face_recognition.compare_faces(encodeList, encode)
        # face distance - the lower the distance the higher the accuracy
        facedis = face_recognition.face_distance(encodeList, encode)
        print(matches)
        print(facedis)
        # to find the minimun facedis from the data
        matchindex = np.argmin(facedis)

        print(matchindex)

        if matches[matchindex]:
            name = stu_name[matchindex]

            # multiply by four bcoz upr size choti kari thi
            current_time = datetime.now()
            y1, x2, y2, x1 = face

            if face not in detected_faces:
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(
                    img,
                    name,
                    (x1 + 6, y2 - 6),
                    cv2.FONT_HERSHEY_COMPLEX,
                    1,
                    (255, 255, 255),
                    2,
                )

                # markAttendance(name)
                # attendance_marked = True
                detected_faces.add(face)
                names = stu_name[matchindex]
                if counter == 0:
                    counter = 1

        if counter != 0:
            if counter == 1:
                studentInfo = db.reference(f"Students/{names}").get()
                datetimeObject = datetime.strptime(
                    studentInfo["Last_Attendance"], "%Y-%m-%d %H:%M:%S"
                )

                totalseconds = (datetime.now() - datetimeObject).total_seconds()

                print(totalseconds)

                if totalseconds > 43200:
                    # update data in the firebase
                    ref = db.reference(f"Students/{names}")
                    studentInfo["Total_Attendance"] += 1
                    ref.child("Total_Attendance").set(studentInfo["Total_Attendance"])
                    ref.child("Last_Attendance").set(
                        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    )
                else:
                    cv2.putText(
                        img,
                        "Attendance is marked already",
                        (x1 + 6, y2 - 6),
                        cv2.FONT_HERSHEY_COMPLEX,
                        1,
                        (255, 255, 255),
                        2,
                    )
            counter += 1

    cv2.imshow("Face Attendance", img)
    if cv2.waitKey(2) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
