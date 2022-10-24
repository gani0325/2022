from pymongo import MongoClient

client = MongoClient("secret!!")
db = client.food


doc = {'name':'taehun','age':28}
db.apple.insert_one(doc)