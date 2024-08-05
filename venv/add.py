import firebase_admin
from firebase_admin import credentials,db

cred = credentials.Certificate("venv\\serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
                              "databaseURL" :"https://visicheck-12e19-default-rtdb.firebaseio.com/"})

ref = db.reference("Students")
data = {
    "Mansi":
    {
        "name" : "Mansi",
        "branch": "CSE",
        "Sec": "B",
        "Year":"3",
        "Id": "22EJCCS129",
        "Last_Attendance":"2024-08-01 00:54:36",
        "Total_Attendance" : 0

    },
    "aayush":
    {
        "name" : "Aayush",
        "branch": "CSE",
        "Sec": "A",
        "Year":"3",
        "Id": "22EJCCS002",
        "Last_Attendance":"2024-08-01 00:34:34",
        "Total_Attendance":0
        

    },
    "Abhijeet":
    {
        "name" : "Abhijeet",
        "branch": "CSE",
        "Sec": "A",
        "Year":"3",
        "Id": "22EJCCS005",
        "Last_Attendance":"2024-08-01 00:34:34",
        "Total_Attendance":0

    },
    "Mansi":
    {
        "name" : "Mansavi",
        "branch": "CSE",
        "Sec": "B",
        "Year":"3",
        "Id": "22EJCCS128",
        "Last_Attendance":"2024-08-01 00:34:34",
        "Total_Attendance":0

    },
    "madhuri":
    {
        "name" : "Madhuri",
        "branch": "CSE",
        "Sec": "B",
        "Year":"3",
        "Id": "22EJCCS127",
        "Last_Attendance":"2024-08-01 00:34:34",
        "Total_Attendance":0

    },
    "hritikroshan":
    {
        "name" : "Hritik",
        "branch": "CSE",
        "Sec": "B",
        "Year":"3",
        "Id": "22EJCCS130",
        "Last_Attendance":"2024-08-01 00:34:34",
        "Total_Attendance":0

    },
    "vicky":
    {
        "name" : "Vicky",
        "branch": "CSE",
        "Sec": "B",
        "Year":"3",
        "Id": "22EJCCS139",
        "Last_Attendance":"2024-08-01 00:34:34",
        "Total_Attendance":0

    },
    "rohitshetty":
    {
        "name" : "Mansi",
        "branch": "CSE",
        "Sec": "B",
        "Year":"3",
        "Id": "22EJCCS129",
        "Last_Attendance":"2024-08-01 00:34:34",
        "Total_Attendance":0

    },




}

for key,value in data.items():
    ref.child(key).set(value)