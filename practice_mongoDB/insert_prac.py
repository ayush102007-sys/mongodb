from pymongo import MongoClient

if __name__ == "__main__":
    print("MongoDB Practices")
    client = MongoClient("mongodb://localhost:27017")

    db = client["quiz-verse"]
    collection = db["results"]

    user_1 = {
        "_id" : "u1",
        "name": "Rajib",
        "topic": "Solar System",
        "score" : 12
    }
    # collection.insert_one(user_1)

    users_1 = [
        {
        "_id" : "u2",
        "name": "Ramu",
        "topic": "FIFA World Cup 2026",
        "score" : 14
        },
        {
        "_id" : "u3",
        "name": "Hitesh",
        "topic": "Freedom Fighters",
        "score" : 11
        } 
    ]
    collection.insert_many(users_1)

    users_2 = [
        {
        "_id" : "u4",
        "name": "Binoy",
        "topic": "FIFA World Cup 2026",
        "score" : 10
        },
        {
        "_id" : "u5",
        "name": "Raheem",
        "topic": "Freedom Fighters",
        "score" : 9
        },
        {
        "_id" : "u6",
        "name": "Ayush",
        "topic": "AI",
        "score" : 15
        }
    ]
    collection.insert_many(users_2)
    