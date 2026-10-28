from pymongo import MongoClient

if __name__ == "__main__":
    print("Welcome to pyMongo")
    client = MongoClient("mongodb://localhost:27017")
    print(client)
    db = client["tset-database"]
    collection = db["test-collection"]

    # To update any data in your db
    prev = {"name": "Tom"}
    nextt = {"$set": {"age": 24}}

    collection.update_one(prev, nextt)  # update one only

    up = collection.update_many(prev, nextt) # update all 

    # To track modified records
    print(up.modified_count)