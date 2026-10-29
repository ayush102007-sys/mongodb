from pymongo import MongoClient

if __name__ == "__main__":
    print("MongoDB Practices")
    client = MongoClient("mongodb://localhost:27017")

    db = client["quiz-verse"]
    collection = db["results"]

    find_1 = collection.find_one({"topic": "Solar System"})
    print(find_1) # prints-> {'_id': 'u1', 'name': 'Rajib', 'topic': 'Solar System', 'score': 12}

    # Now I want to update topic "Solar System" to "AI"

    up_1 = collection.update_one({"_id": "u1"}, {"$set": {"topic": "AI"}})

    # Now assume that a doc doesn't exist in your collection. You can use "upsert" (insert -> update)

    up_2 = collection.update_one({"_id": "u7", "name": "Aloy", "score": 12}, {"$set": {"topic": "Solar System"}}, upsert=True)

    # The "$push" operator adds a new value to an array field.

    up_3 = collection.update_one({"_id": "scores"}, {"$push": {"result_list": 12}})
    