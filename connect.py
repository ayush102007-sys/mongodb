from pymongo import MongoClient

if __name__ == "__main__":
    print("Welcome to pyMongo")
    client = MongoClient("mongodb://localhost:27017")
    print(client)
    