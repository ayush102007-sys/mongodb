# MongoDB Learning Journey 🚀

> This repository is my complete learning path for MongoDB, with a focus on connecting Python applications to MongoDB using **PyMongo** and understanding the essential CRUD operations.

MongoDB is a popular **NoSQL database** that stores data in **documents** rather than traditional rows and tables. It is especially useful when working with flexible, JSON-like data structures, fast development cycles, and scalable applications.

This project is a practical study guide that helps beginners understand how MongoDB works and how to use it from Python.

## Why MongoDB? 📚

MongoDB is widely used in modern web and application development because it is:

- Flexible and schema-less
- Easy to store JSON-like data
- Great for fast prototyping
- Suitable for real-world apps with evolving data structures

It is also a strong choice for Python developers who want to build apps that interact with data efficiently.

## Core Concepts 🧠

### 1) MongoDB Compass 🖥️
MongoDB Compass is the official graphical interface for MongoDB. It lets you visually explore databases, collections, and documents without writing complex commands.

It is especially helpful for beginners because you can see how data is stored and structured in real time.

**Download MongoDB Compass for free:**
[MongoDB Compass Download](https://www.mongodb.com/try/download/community)

### 2) mongod vs MongoDB vs MongoDB Compass
Here is the difference between the main pieces involved in MongoDB:

| Component | What it is | Main purpose |
|---|---|---|
| `mongod` | The MongoDB server daemon | Runs the database and handles storage, connections, and queries |
| MongoDB | The database itself | Stores data in documents using BSON, which is a binary version of JSON |
| MongoDB Compass | The GUI tool | Helps users visually inspect and manage databases |

In simple words, `mongod` is the server, MongoDB is the database engine, and Compass is the friendly visual tool used to interact with it.

### 3) CRUD Operations 🔁
CRUD stands for:

- **Create**: Add new data
- **Read**: Fetch or view existing data
- **Update**: Modify existing records
- **Delete**: Remove data

These four operations are the foundation of almost every database interaction. Understanding CRUD is essential before moving to advanced queries, indexing, or application development.

You can also explore MongoDB’s official learning resources:
[CRUD Operations Skill Badge (Free)](https://learn.mongodb.com/courses/crud-operations-in-mongodb)

### 4) Mongo Shell Commands 💻
The `mongosh` shell is the command-line interface for MongoDB. It allows developers to interact with the database directly.

```bash
show dbs // List all databases
use ecommerce // Create or switch to a database
show collections // List all collections in the current DB
db.dropDatabase() // Drop current database
```

This is useful when you want to test queries quickly or inspect the database without using a graphical interface.

## PyMongo 🐍
**PyMongo** is the official Python driver for MongoDB. It allows Python applications to connect to MongoDB, insert records, fetch documents, update data, and delete records easily.

### Install PyMongo
Open your terminal and run:

```bash
pip install pymongo
```

### 1) Connect to MongoDB
This example creates a connection to the local MongoDB server.

[MongoDB connection](connect.py)

### 2) Insert Documents
This script shows how to create a database and collection, then insert one or many records.

[MongoDB insert](insert.py)

### 3) Find Documents
This script demonstrates how to query one document, multiple documents, and filtered records.

[MongoDB find](find.py)

### 4) Show Databases and Collections
This example explains how to list available databases and collections.

[MongoDB show](show_db_col.py)

### 5) Update Records
This script shows how to update one document or many documents in a collection.

[MongoDB update](update.py)

### 6) Delete Records
This example demonstrates how to remove one record or multiple records from a collection.

[MongoDB delete](delete.py)

## Practice Folder 🧪
The `practice_mongoDB` folder contains hands-on exercises for CRUD operations and query examples. These scripts are meant to reinforce the learning by practicing real MongoDB queries in Python.

Examples in this folder include:

- insert examples
- find and filter examples
- projection examples
- update examples
- delete examples

## Learning Goals 🎯
By the end of this project, the aim is to understand:

- how MongoDB stores data
- how to connect Python to MongoDB using PyMongo
- how to perform CRUD operations
- how to query and filter data effectively
- how to work with collections and documents in real projects

## Final Note 💡
This repository is a beginner-friendly MongoDB learning project. It focuses on practical examples so the concepts are easier to understand and apply in future Python projects, including Flask-based applications.

If you are learning MongoDB for the first time, this project is a great starting point because it keeps the examples simple, direct, and easy to follow.
