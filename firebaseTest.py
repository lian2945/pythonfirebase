import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('secrets.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://test2-b201e-default-rtdb.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('button/button1')
print(ref.get())

ref2 = db.reference()
ref2.update({"Student" : {"ID" : "1401", "Name" : "김동욱", "Score" : "0"}})