from pymongo import MongoClient

client = MongoClient("YOUR_ATLAS_URI")

db = client["edr_db"]

logs_collection = db["logs"]
alerts_collection = db["alerts"]
users_collection = db["users"]