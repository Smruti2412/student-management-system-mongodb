from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["student_db"]

students = db["students"]
users = db["users"]

# Create default admin if not exists
if users.count_documents({"username": "admin"}) == 0:
    users.insert_one({
        "username": "admin",
        "password": "admin123"
    })
