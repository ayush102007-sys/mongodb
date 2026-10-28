from pymongo import MongoClient

if __name__ == "__main__":
    print("Welcome to pyMongo")
    client = MongoClient("mongodb://localhost:27017")
    print(client)

    # To see all the databases created (list format)
    allDatabases = client.list_database_names()
    print(allDatabases)

    # To see your collections inside your db
    col = client["firstdb"]
    print(col.list_collection_names())