from pymongo import MongoClient

if __name__ == "__main__":
    print("MongoDB Practices")
    client = MongoClient("mongodb://localhost:27017")

    db = client["quiz-verse"]
    collection = db["results"]

    # If we want to exclude or include data/records after querying db, we use projection method.

    # 1. INCLUSION METHOD 
    incl_Docs = collection.find({"score": {"$gte": 10}}, {"name":1, "topic":1})
    for rec_1 in incl_Docs:
        print(rec_1)

    # 2. EXCLUSION METHOD 
    excl_Docs = collection.find({"score": {"$gte": 10}}, {"name":0})
    for rec_2 in excl_Docs:
        print(rec_2)

    # WE CAN'T USE INCLUSION & EXCLUSION TOGETHER

    all_Docs = collection.find({"score": {"$gte": 10}}, {"name":0, "score":1})
    for rec_3 in all_Docs:
        print(rec_3)  # Cannot do inclusion on field score in exclusion projection. ERROR!
        
    # But WAIT! There's an exception with _id field.. That can be executed as INCLUSION + EXCLUSION.
    excep_doc = collection.find({"score": {"$gt": 10}}, {"name":1, "_id": 0})
    for rec_4 in excep_doc:
        print(rec_4)

        