#Title: Jaggernauth_usersp1.py
##Author: Amit Jaggernauth
###Date: 2/25/2026
####Description: Hands-On 4.2


# Import the MongoClient
from pymongo import MongoClient

# Build a connection string to connect to MongoDB Atlas
client = MongoClient(
    "mongodb+srv://web335_user:s3cret@cluster0.lujih.mongodb.net/web335DB?retryWrites=true&w=majority"
)

# Print the client object to confirm connection
print(client)

# Configure a variable to access the web335DB
db = client["web335DB"]

# Display all documents in the users collection
for user in db.users.find({}):
    print(user)

# Display a document where employeeId is 1011
print(db.users.find_one({"employeeId": "1011"}))

# Display a document where lastName is Mozart
print(db.users.find_one({"lastName": "Mozart"}))