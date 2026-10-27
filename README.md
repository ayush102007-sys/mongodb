# MongoDB Learning 

> This documentation is a complete learning journey of MongoDB and how I am going to connect my Flask apps' database using **pyMongo**.

## Topics 
These following topics I will learn about **MongoDB**.
### Fundamentals

1. Installation of MongoDB Compass
> MongoDB Compass is the free, official graphical user interface (GUI) for MongoDB that lets you visually explore, query, and manage your database.
**Link to download _free_ MongoDB Compass** - 
[MongoDB Compass Download](https://www.mongodb.com/try/download/community)

2. mongod vs MongoDB vs MongoDB Compass
> The following comparisson table will definitely help you to see the differences among them.

| mongod | MongoDB | MongoDB Compass |
|---:| ----|---| 
|the **main MongoDB server daemon**. It handles connections, database storage, and queries. You must run this before using MongoDB locally| a **NoSQL document-oriented database**. It stores data in **JSON-like documents** (actually **BSON**, a binary form of JSON). |a **GUI tool** for visualizing data, running queries, and analyzing performance. Perfect for beginners who prefer a graphical view.| 

3. CRUD Operations
> CRUD operations **(Create, Read, Update, Delete)** form the foundational backbone of interacting with data in MongoDB.

Will learn more about CRUD operations in details later.
You can also refer to the official **Skill Badge Course on MongoDB University** by this link-
[CRUD Operations Skill Badge (Free)](https://learn.mongodb.com/courses/crud-operations-in-mongodb)

4. Basic Mongo Shell Commands
> `mongosh` - the MongoDB Shell. It's **command-line interface** for
interacting with MongoDB. You use it to run commands, queries, and scripts.
```bash
show dbs // List all databases
use ecommerce // Create or switch to a database
show collections // List all collections in the current DB
db.dropDatabase() // Drop current database
```

## pyMongo
**PyMongo** is a Python distribution containing tools for working with MongoDB, and is the recommended way to work with MongoDB from Python.

1. Install pyMongo

Open the terminal and write-
```bash
pip install pymongo
```

2. Connection to database
You will find the code here-

[MongoDB connection](connect.py)

3. Insertion of Documents
You will find the code here-

[MongoDB insert](insert.py)

4. Finding document in your database
You will find the code here-

[MongoDB find](find.py)

