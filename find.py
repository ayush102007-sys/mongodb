from pymongo import MongoClient

if __name__ == "__main__":
    print("Welcome to pyMongo")
    client = MongoClient("mongodb://localhost:27017")
    db = client["tset-database"]
    collection = db["test-collection"]

    # Pulling one document (It is a random process)
    one = collection.find_one()
    print(one)

    # Pulling/Finding a specific document by using keys
    sp_one = collection.find_one({"name":"Ankush"})
    print(sp_one)

    # Pulling multiple documents 
    allDocs = collection.find({"name": "Ankush"})
    for item in allDocs:
        print(item)

    # To get specific fields form your document
    sp_docs = collection.find({"name": "Ankush"}, {"name": 1, "_id": 0})
    for field in sp_docs:
            print(field)    