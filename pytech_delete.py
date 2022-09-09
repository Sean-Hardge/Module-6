#!/usr/bin/env python

import pymongo

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db = connection.school
students = db.students


def find():
    print("find, reporting for duty")


def find_one():
    print("find one, reporting for duty")


def delete_one():
    print("delete, reporting for duty")


def delete_many():
    print("delete many, reporting for duty")


if __name__ == '__main__':
    find()
    find_one()
    delete_one()
    delete_many()

# this code is slightly different from the example we saw
# in the video, but it works just as well
query = {'last_name': 'smith'}

students.delete_many(query)

# now, we'll re-query the database to see if the deletion
# worked
query = {'last_name': 'smith'}

cursor = students.find(query)

# iterate over the results and print each document
for doc in cursor:
    print(doc)

# now, let's delete a single document
query = {'last_name': 'smith'}

result = students.delete_one(query)
print(result.deleted_count)

# now, we'll re-query the database to see if the deletion
# worked
query = {'last_name': 'smith'}

cursor = students.find(query)

# iterate over the results and print each document
for doc in cursor:
    print(doc)

# let's delete all documents with a last name of 'smith'
query = {'last_name': 'smith'}

result = students.delete_many(query)
print(result.deleted_count)
