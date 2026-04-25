from db import users

users.insert_one({
    "username": "admin",
    "password": "admin123"
})

print("User created successfully")