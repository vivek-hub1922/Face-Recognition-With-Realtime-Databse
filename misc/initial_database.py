import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("../serviceAccountKey.json")
firebase_admin.initialize_app(
    cred,
    {
        "databaseURL": "https://face-detect-5da30-default-rtdb.firebaseio.com/",
        # database URL
    },
)

ref = db.reference(
    "Students"
)  # reference path to our database... will create student directory in the database

data = {
    "1RD19MCA38":{  # id of student which is a key
        "id": "1RD19MCA38",
        "name": "Vivek",
        "password": "1RD19MCA38",
        "dob": "1997-08-02",
        "address": "Ranchi",
        "phone": "8969567408",
        "email": "vivek@gmail.com",
        "major": "MCA",
        "starting_year": 2020,
        "standing": "G",
        "total_attendance": 4,
        "year": 2,
        "last_attendance_time": "2023-02-21 12:33:10",
        "content": "This section aims to offer essential guidance for students to successfully complete the course. It will be regularly updated \
                to ensure its relevance and usefulness. Stay tuned for valuable \
                insights and tips that will help you excel in your studies.",
    },
}


for key, value in data.items():
    ref.child(key).set(value)
