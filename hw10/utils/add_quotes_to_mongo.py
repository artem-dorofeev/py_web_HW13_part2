import json
from bson.objectid import ObjectId

from pymongo import MongoClient


client = MongoClient("mongodb://localhost")

db = client.hw


with open('quotes.json', 'r', encoding='utf-8') as fdb:
    quotes = json.load(fdb)

for quote in quotes:
    author = db.authors.find_one({'fullname': quote['author']})
    if author:
        db.quotes.insert_one({
            'quote': quote['quote'],
            'tags': quote['tags'],
            'author': ObjectId(author['_id'])
        })