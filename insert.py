from pymongo import MongoClient

if __name__ == "__main__":
    print("Welcome to pyMongo")
    client = MongoClient("mongodb://localhost:27017")

    # Creating database
    db = client["tset-database"]
    # Creating collection
    collection = db["test-collection"]

    # Insert one
    dictionary = {"name": "Ayush", "marks": 50}
    collection.insert_one(dictionary)

    # Insert many
    dict2 = [
        {"name": "Ankush", "age": 19, "country": "India"},
        {"name": "Tom", "age": 21, "country": "England"},
        {"name": "Saleem", "age": 16, "country": "Bangladesh"}
    ]
    collection.insert_many(dict2)

    dict3 = [
            {"_id": 1,"name": "Ankush", "age": 19, "country": "India"},
            {"_id": 2,"name": "Tom", "age": 21, "country": "England"},
            {"_id": 3,"name": "Saleem", "age": 16, "country": "Bangladesh"}
        ]
    collection.insert_many(dict3)

