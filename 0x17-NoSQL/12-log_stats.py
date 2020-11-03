#!/usr/bin/env python3
"""module"""


from pymongo import MongoClient


client = MongoClient('mongodb://127.0.0.1:27017')
col = client.logs.nginx

x = col.find()
print(x, "logs")
print("Methods:")
for i in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
    print('\tmethod ', i, ': 'len(col.find({method: i})))
print(len(col.find({method: "GET"}, {path, "/status"})), " status check")
