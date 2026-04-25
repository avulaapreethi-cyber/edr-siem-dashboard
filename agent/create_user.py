from db import users_collection
from werkzeug.security import generate_password_hash

username = "admin"
password = generate_password_hash("admin123")

users_collection.insert_one({
    "username": username,
    "password": password
})

print("✅ User created: admin / admin123")