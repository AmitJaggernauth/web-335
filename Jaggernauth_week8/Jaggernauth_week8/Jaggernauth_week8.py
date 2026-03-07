
#Title: whatabook_install.py
##Author: Amit Jaggenrauth
##Date: Assignment 8.2


from pymongo import MongoClient

# 1. Connect to MongoDB Atlas

client = MongoClient(
    "mongodb+srv://web335_user:s3cret@cluster0.lujih.mongodb.net/"
    "retryWrites=true&w=majority"
)

db = client["whatabook"]

# 2. Drop existing collections

db.books.drop()
db.customers.drop()
db.wishlistitems.drop()

# 3. Insert Books

books = [
    {
        "_id": "b1001",
        "bookId": 1001,
        "title": "The Great Gatsby",
        "genre": "Fiction",
        "author": "F. Scott Fitzgerald"
    },
    {
        "_id": "b1002",
        "bookId": 1002,
        "title": "Dune",
        "genre": "Sci-Fi",
        "author": "Frank Herbert"
    },
    {
        "_id": "b1003",
        "bookId": 1003,
        "title": "Pride and Prejudice",
        "genre": "Romance",
        "author": "Jane Austen"
    }
]

db.books.insert_many(books)

# 4. Insert Customers

customers = [
    {
        "_id": "c1",
        "customerId": "c1007",
        "firstName": "Emily",
        "lastName": "Carter"
    },
    {
        "_id": "c2",
        "customerId": "c1008",
        "firstName": "Lucas",
        "lastName": "Andrade"
    },
    {
        "_id": "c3",
        "customerId": "c1009",
        "firstName": "Robert",
        "lastName": "Martinez"
    }
]

db.customers.insert_many(customers)

# 5. Insert Wishlist Items

wishlistitems = [
    {
        "_id": "w1",
        "customerId": "c1007",
        "bookId": 1002
    },
    {
        "_id": "w2",
        "customerId": "c1008",
        "bookId": 1001
    }
]

db.wishlistitems.insert_many(wishlistitems)

print("WhatABook database installation complete.\n")

# 6. Showcase Queries

print("1. List of all books:")
for book in db.books.find():
    print(book)

print("\n2. Books by genre (Sci-Fi):")
for book in db.books.find({"genre": "Sci-Fi"}):
    print(book)

print("\n3. Books by author (Jane Austen):")
for book in db.books.find({"author": "Jane Austen"}):
    print(book)

print("\n4. Book by bookId (1002):")
print(db.books.find_one({"bookId": 1002}))