from pymongo import MongoClient, ASCENDING, DESCENDING

if __name__ == "__main__":
    print("MongoDB Practices")
    client = MongoClient("mongodb://localhost:27017")

    db = client["quiz-verse"]
    collection = db["results"]

    # using a specific key
    result_1 = collection.find({"topic": "FIFA World Cup 2026"})
    for rec_1 in result_1:
        print(rec_1)

    # using comparison operators (gt,gte,lt,lte,eq,ne)
    result_2 = collection.find({"topic": "FIFA World Cup 2026", "score": {"$gt": 10}})
    for rec_2 in result_2:
        print(rec_2["name"])

    # using logical operators (and,or,not,nor)
    result_3 = collection.find({
        "$and": [
            {"topic": "Freedom Fighters"},
            {"score": {"$lte":12}}
        ]
    })
    for rec_3 in result_3:
        print(rec_3["name"])

    # a) Special uses:- (explicit use of and with other operators)
    result_3_1 = collection.find({
        "$and": [
            {
                "$or" : [
                    {"key1": "val1"},
                    {"key2": "val2"}
                ]},
            {
                "$or" : [
                    {"key1": "val1"},
                    {"key2": "val2"}
                ]}
        ]})

    # using membership operators (in, not in)
    result_4 = collection.find({
        "topic": {"$in": ["Solar System", "AI"]}
    })

    for rec_4 in result_4:
        print(rec_4["score"])

    # sorting 
    result_5 = collection.find().sort("score", DESCENDING)

    for rec5 in result_5:
        print(rec5["name"])