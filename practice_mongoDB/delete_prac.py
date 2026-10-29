from pymongo import MongoClient

if __name__ == "__main__":
    print("MongoDB Practices")
    client = MongoClient("mongodb://localhost:27017")

    db = client["quiz-verse"]
    collection = db["results"]

    collection.delete_one({"_id": "u1"})

    collection.delete_many({"topic": "Freedom Fighters"}) # deletes records with topic: Freedom Fighters