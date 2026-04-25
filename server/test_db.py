from pymongo import MongoClient

MONGO_URI = "mongodb+srv://admin:Admin123@cluster0.cyehtiy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0&authSource=admin"

client = MongoClient(MONGO_URI)

# Database
db = client["edr_logs"]

# Collections
logs = db["logs"]
users = db["users"]