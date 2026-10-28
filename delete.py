from pymongo import MongoClient

if __name__ == "__main__":
    print("Welcome to pyMongo")
    client = MongoClient("mongodb://localhost:27017")
    db = client["tset-database"]
    collection = db["test-collection"]

    # To delete any records from your db
    rec = {"name": "Tom"}
    collection.delete_one(rec)  # only one

    delete = collection.delete_many(rec) # delete multiple records

    # To count deleted records
    print(delete.deleted_count)
    