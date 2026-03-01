#Title: Jaggernauth_usersp1.py
##Author: Amit Jaggernauth
###Date: 2/28/2026
####Description: Hands-On 5.2

from pymongo import MongoClient

# Connect to MongoDB Atlas
client = MongoClient(
    "mongodb+srv://web335_user:s3cret@cluster0.lujih.mongodb.net/web335DB?retryWrites=true&w=majority"
)

db = client['web335DB']
users = db.users

# 1. Create a new user document
new_user = {
    "firstName": "Kevin",
    "lastName": "Smith",
    "employeeId": "1007",
    "email": "ksmith@myemail.com"
}

create_result = users.insert_one(new_user)
print(f"Inserted ID: {create_result.inserted_id}")

# 2. Prove the document was created
created_doc = users.find_one({"employeeId": "1007"})
print(created_doc)

# 3. Update the email address
update_result = users.update_one(
    {"employeeId": "1007"},
    {"$set": {"email": "ksmith123@myemail.com"}}
)

print(f"Matched: {update_result.matched_count}, Modified: {update_result.modified_count}")

# 4. Prove the document was updated
updated_doc = users.find_one({"employeeId": "1007"})
print(updated_doc)

# 5. Delete the document
delete_result = users.delete_one({"employeeId": "1007"})
print(f"Deleted Count: {delete_result.deleted_count}")

# 6. Prove the document was deleted
deleted_check = users.find_one({"employeeId": "1007"})
print(deleted_check)  # Should print None